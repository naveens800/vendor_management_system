from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from .models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_on_save(sender, instance, created, **kwargs):
    PurchaseOrder.objects.update_on_time_delivery_rate(instance)
        
