from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    """
    API Endpoints:
    ● POST /api/vendors/: Create a new vendor.
    ● GET /api/vendors/: List all vendors.
    ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
    ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
    ● DELETE /api/vendors/{vendor_id}/: Delete a vendor
    """
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        return Vendor.objects.all()
