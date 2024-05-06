from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from .models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_on_save(sender, instance, created, **kwargs):
    """
    Signal handler that updates vendor performance metrics after a PurchaseOrder instance is saved.

    This function is a handler for the post_save signal of the PurchaseOrder model. It is called 
    after a PurchaseOrder instance is saved. Depending on specific conditions and requirements, 
    it will update relevant vendor performance metrics (e.g., on_time_delivery_rate, quality_rating_avg,
    average_response_time, and fulfillment_rate).

    - Parameters:
        sender (type): The PurchaseOrder model class that triggered this signal.
        instance (PurchaseOrder): The specific instance of the PurchaseOrder that was saved.
        created (bool): Boolean flag indicating whether this is a new instance (True) or an update (False).
        **kwargs: Additional keyword arguments that are passed through from the signal.
    
    - Behavior:
        - Calls a method on the instance (e.g., update_on_time_delivery_rate) to update metrics
          based on the most recent information available.
    """
    PurchaseOrder.objects.update_appropriate_metrics(instance)
        
