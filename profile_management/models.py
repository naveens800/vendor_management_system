from django.db import models
from django.core.exceptions import ValidationError


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def clean(self):
        if not self.name:
            raise ValidationError(_("Name cannot be empty."))
        if not self.contact_details:
            raise ValidationError(_("Contact details cannot be empty."))
        if not self.address:
            raise ValidationError(_("Address cannot be empty."))
        if not self.vendor_code:
            raise ValidationError(_("Vendor code cannot be empty."))

    def __str__(self):
        return self.name
