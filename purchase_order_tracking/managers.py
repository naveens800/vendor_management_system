from django.db import models
from django.db.models import Avg, ExpressionWrapper, F, fields
from django.utils import timezone
from performance_evaluation.models import VendorPerformanceRecord


def timedelta_to_hours(td):
    return td.total_seconds() / 3600.0


class PurchaseOrderManager(models.Manager):
    """
    Manager class for handling business logic and calculations related to Purchase Orders.

    This class contains methods that are responsible for:
    - Updating the on-time delivery rate, quality rating average, average response time, and fulfillment rate
      for vendors based on the status of their purchase orders.
    - Calculating the various performance metrics to keep the vendor's performance records updated.
    """

    def update_appropriate_metrics(self, instance):
        on_time_delivery_rate = self.calculate_on_time_delivery_rate(instance)
        quality_rating_avg = self.calculate_quality_rating_avg(instance)
        avg_response_time = self.calculate_average_response_time(instance)
        fulfillment_rate = self.calculate_fulfillment_rate(instance)

        self.update_vendor_performance_record(
            instance,
            on_time_delivery_rate,
            quality_rating_avg,
            avg_response_time,
            fulfillment_rate,
        )

    def calculate_on_time_delivery_rate(self, instance):
        if instance.status == self.model.Status.COMPLETED:
            completed_purchases = (
                self.select_related("vendor")
                .filter(
                    vendor=instance.vendor,
                    status=self.model.Status.COMPLETED,
                    delivery_date__lte=F("delivery_date"),
                )
                .count()
            )

            total_completed_purchases = (
                self.select_related("vendor")
                .filter(vendor=instance.vendor, status=self.model.Status.COMPLETED)
                .count()
            )

            return (
                (completed_purchases / total_completed_purchases) * 100
                if total_completed_purchases > 0
                else 0
            )

    def calculate_quality_rating_avg(self, instance):
        if instance.status == self.model.Status.COMPLETED and instance.quality_rating:
            return (
                self.select_related("vendor")
                .filter(
                    quality_rating__isnull=False,
                    vendor=instance.vendor,
                    status=self.model.Status.COMPLETED,
                )
                .aggregate(Avg("quality_rating", default=None))["quality_rating__avg"]
            )

    def calculate_average_response_time(self, instance):
        if instance.acknowledgment_date:
            response_time_avg = (
                self.select_related("vendor")
                .filter(vendor=instance.vendor, acknowledgment_date__isnull=False)
                .annotate(
                    response_time=ExpressionWrapper(
                        F("acknowledgment_date") - F("issue_date"),
                        output_field=fields.DurationField(),
                    )
                )
                .aggregate(Avg("response_time", default=None))["response_time__avg"]
            )

            # Convert timedelta to hours (or another unit) if it exists
            if response_time_avg:
                return timedelta_to_hours(response_time_avg)
            else:
                return None

        else:
            return None

    def calculate_fulfillment_rate(self, instance):
        total_purchase_orders = instance.vendor.purchaseorder_set.count()
        fulfilled_purchase_orders = instance.vendor.purchaseorder_set.filter(
            status=self.model.Status.COMPLETED
        ).count()

        return (
            (fulfilled_purchase_orders / total_purchase_orders) * 100
            if total_purchase_orders > 0
            else 0
        )

    def update_vendor_performance_record(
        self,
        instance,
        on_time_delivery_rate,
        quality_rating_avg,
        avg_response_time,
        fulfillment_rate,
    ):
        VendorPerformanceRecord.objects.update_or_create(
            vendor=instance.vendor,
            date=timezone.now(),
            defaults={
                "on_time_delivery_rate": on_time_delivery_rate or 0,
                "quality_rating_avg": quality_rating_avg or 0,
                "average_response_time": avg_response_time or 0,
                "fulfillment_rate": fulfillment_rate or 0,
            },
        )
