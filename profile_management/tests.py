from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from profile_management.models import Vendor


class VendorAPITest(TestCase):
    def setUp(self):
        # Create an APIClient instance
        self.client = APIClient()

        # Define the URLs
        self.vendor_list_url = reverse("vendor-list")
        self.vendor_detail_url = lambda pk: reverse(
            "vendor-detail", kwargs={"vendor_id": pk}
        )

        # Create a sample vendor instance
        self.vendor = Vendor.objects.create(
            name="Sample Vendor",
            contact_details="sample@example.com",
            address="123 Vendor Street",
            vendor_code="SAMPLE123",
            on_time_delivery_rate=98.5,
            quality_rating_avg=4.2,
            average_response_time=24.7,
            fulfillment_rate=96.4,
        )

    def test_list_vendors(self):
        response = self.client.get(self.vendor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)

    def test_create_vendor(self):
        new_vendor_data = {
            "name": "New Vendor",
            "contact_details": "newvendor@example.com",
            "address": "456 Vendor Avenue",
            "vendor_code": "NEW456",
            "on_time_delivery_rate": 99.2,
            "quality_rating_avg": 4.8,
            "average_response_time": 22.1,
            "fulfillment_rate": 97.8,
        }
        response = self.client.post(
            self.vendor_list_url, data=new_vendor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["name"], new_vendor_data["name"])

    def test_retrieve_vendor(self):
        response = self.client.get(self.vendor_detail_url(self.vendor.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], self.vendor.name)

    def test_update_vendor(self):
        updated_data = {
            "name": "Updated Vendor",
            "contact_details": "updated@example.com",
            "address": "Updated Address 789",
            "vendor_code": "UPDATED123",
            "on_time_delivery_rate": 97.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 21.5,
            "fulfillment_rate": 95.2,
        }
        response = self.client.put(
            self.vendor_detail_url(self.vendor.pk), data=updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], updated_data["name"])

    def test_delete_vendor(self):
        response = self.client.delete(self.vendor_detail_url(self.vendor.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vendor.objects.filter(pk=self.vendor.pk).exists())
