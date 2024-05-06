from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from rest_framework import status
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    """
    API Endpoints:
    ● POST /api/purchase_orders/: Create a purchase order.
    ● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
    ● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    ● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    ● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
    """

    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = "po_id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
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
        return PurchaseOrder.objects.all()


@api_view(["POST"])
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(po_number=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Update the acknowledgment_date
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()
    return Response(status=status.HTTP_200_OK)
