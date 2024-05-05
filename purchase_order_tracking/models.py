from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .managers import PurchaseOrderManager


class PurchaseOrder(models.Model):
    class Status(models.TextChoices):
        COMPLETED = "COMPLETED", _("Completed")
        PENDING = "PENDING", _("Pending")
        CANCELLED = "CANCELLED", _("Cancelled")

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey("profile_management.Vendor", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=Status.choices)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    objects = PurchaseOrderManager()

    def clean(self):
        if self.delivery_date < self.order_date:
            raise ValidationError(_("Delivery date cannot be before order date."))
        if not isinstance(self.items, list):
            raise ValidationError(_("Items must be a list."))
        if self.quantity <= 0:
            raise ValidationError(_("Quantity must be a positive integer."))
        if self.status not in dict(self.Status.choices):
            raise ValidationError(_("Invalid status."))
        if self.quality_rating is not None and not (0.0 <= self.quality_rating <= 5.0):
            raise ValidationError(_("Quality rating must be between 0.0 and 5.0."))
        if self.issue_date > timezone.now():
            raise ValidationError(_("Issue date cannot be in the future."))
        if self.acknowledgment_date and self.acknowledgment_date > timezone.now():
            raise ValidationError(_("Acknowledgment date cannot be in the future."))
        if self.acknowledgment_date and self.acknowledgment_date < self.issue_date:
            raise ValidationError(_("Acknowledgment date cannot be before issue date."))

    def __str__(self):
        return self.po_number
