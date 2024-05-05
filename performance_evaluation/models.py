from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class VendorPerformanceRecord(models.Model):
    vendor = models.ForeignKey("profile_management.Vendor", on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def clean(self):
        if self.date > timezone.now():
            raise ValidationError(_("Date cannot be in the future."))

    def __str__(self):
        return f"{self.vendor} - {self.date}"
