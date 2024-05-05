from django.urls import path, include
from rest_framework.routers import DefaultRouter
from purchase_order_tracking import views

router = DefaultRouter()
router.register(r'purchase_orders', views.PurchaseOrderViewSet, basename='purchaseorder')

urlpatterns = [
    path('', include(router.urls)),
    path('purchase_orders/<str:po_id>/acknowledge', views.acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
