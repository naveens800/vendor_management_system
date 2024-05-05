from rest_framework import serializers
from .models import VendorPerformanceRecord
from profile_management.serializers import VendorSerializer

class VendorPerformanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPerformanceRecord
        fields = ('vendor', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')