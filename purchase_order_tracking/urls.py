from django.urls import path, include
from rest_framework.routers import DefaultRouter
from purchase_order_tracking import views

router = DefaultRouter()
router.register(r'purchase_orders', views.PurchaseOrderViewSet, basename='purchaseorder')

urlpatterns = [
    path(
        "purchase_orders/<int:po_id>/",
        views.PurchaseOrderViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="vendor-detail",
    ),
    path('purchase_orders/<int:po_id>/acknowledge', views.acknowledge_purchase_order, name='acknowledge_purchase_order'),
]

urlpatterns += router.urls