from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone
from profile_management.models import Vendor
from performance_evaluation.models import VendorPerformanceRecord


class VendorPerformanceAPITest(TestCase):
    def setUp(self):
        # Initialize test client
        self.client = APIClient()

        # Create a sample vendor
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

        # Create sample performance records for the vendor
        self.performance_record = VendorPerformanceRecord.objects.create(
            vendor=self.vendor,
            date=timezone.now() - timezone.timedelta(days=7),
            on_time_delivery_rate=96.7,
            quality_rating_avg=4.5,
            average_response_time=20.1,
            fulfillment_rate=94.3,
        )

        # URL for vendor performance API
        self.vendor_performance_url = reverse(
            "vendor-performance", kwargs={"vendor_id": self.vendor.pk}
        )

    def test_vendor_performance_success(self):
        response = self.client.get(self.vendor_performance_url)
        self.assertGreater(len(response.json()), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["vendor"], self.vendor.pk)
        self.assertEqual(
            response.json()[0]["on_time_delivery_rate"],
            self.performance_record.on_time_delivery_rate,
        )

    def test_vendor_performance_not_found(self):
        invalid_vendor_url = reverse(
            "vendor-performance", kwargs={"vendor_id": 9999}
        )  # A non-existent vendor ID
        response = self.client.get(invalid_vendor_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
