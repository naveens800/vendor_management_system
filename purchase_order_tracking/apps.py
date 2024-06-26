from django.apps import AppConfig


class PurchaseOrderTrackingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purchase_order_tracking'
    
    def ready(self) -> None:
        from purchase_order_tracking import signals
