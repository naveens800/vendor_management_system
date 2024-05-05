from rest_framework import serializers
from .models import PurchaseOrder
from profile_management.serializers import VendorSerializer
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ('id', 'vendor', 'po_number', 'order_date', 'delivery_date',
                  'items', 'quantity', 'status', 'quality_rating', 'issue_date',
                  'acknowledgment_date')
