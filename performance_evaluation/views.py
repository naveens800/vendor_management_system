from rest_framework.response import Response
from .serializers import VendorPerformanceRecordSerializer
from profile_management.models import Vendor
from performance_evaluation.models import VendorPerformanceRecord
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view



@api_view(['GET'])
def vendor_performance(request, vendor_id):
    # Retrieve the vendor object or return 404 if not found
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    # Retrieve related performance records for the vendor
    performance_records = VendorPerformanceRecord.objects.filter(vendor=vendor)

    # Serialize vendor performance data
    serializer = VendorPerformanceRecordSerializer(performance_records, many=True)

    # Return the serialized data
    return Response(serializer.data)