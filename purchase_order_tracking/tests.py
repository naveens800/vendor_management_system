from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from purchase_order_tracking.models import PurchaseOrder
from profile_management.models import Vendor


class PurchaseOrderViewSetTests(APITestCase):
    def setUp(self):
        # Setup common data
        self.vendor = Vendor.objects.create(
            name="Sample Vendor",
            contact_details="vendor@example.com",
            address="Vendor Address",
            vendor_code="V12345",
            on_time_delivery_rate=98.5,
            quality_rating_avg=4.2,
            average_response_time=24.7,
            fulfillment_rate=96.4,
        )
        self.purchase_order_data = {
            "po_number": "PO123",
            "vendor_id": self.vendor.id,
            "order_date": timezone.now(),
            "delivery_date": timezone.now() + timezone.timedelta(days=10),
            "items": ["Item1", "Item2"],
            "quantity": 5,
            "status": "PENDING",
            "issue_date": timezone.now(),
        }
        self.purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)

    def test_list_purchase_orders(self):
        url = reverse("purchaseorder-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)

    def test_retrieve_purchase_order(self):
        url = reverse("purchaseorder-detail", kwargs={"po_id": self.purchase_order.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["po_number"], self.purchase_order.po_number)

    def test_create_purchase_order(self):
        url = reverse("purchaseorder-list")
        data = {
            "po_number": "PO456",
            "vendor": self.vendor.id,
            "order_date": timezone.now(),
            "delivery_date": timezone.now() + timezone.timedelta(days=10),
            "items": ["ItemA", "ItemB"],
            "quantity": 10,
            "status": "PENDING",
            "issue_date": timezone.now(),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_purchase_order(self):
        url = reverse("purchaseorder-detail", kwargs={"po_id": self.purchase_order.pk})
        updated_data = {
            "po_number": "PO123",
            "vendor": self.vendor.id,
            "order_date": timezone.now(),
            "delivery_date": timezone.now() + timezone.timedelta(days=10),
            "items": ["Item1", "Item2"],
            "quantity": 5,
            "status": "PENDING",
            "issue_date": timezone.now(),
        }

        updated_data["status"] = "COMPLETED"
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            PurchaseOrder.objects.get(pk=self.purchase_order.pk).status, "COMPLETED"
        )

    def test_delete_purchase_order(self):
        url = reverse("purchaseorder-detail", kwargs={"po_id": self.purchase_order.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            PurchaseOrder.objects.filter(pk=self.purchase_order.pk).exists()
        )
