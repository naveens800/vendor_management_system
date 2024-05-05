import json
from datetime import datetime, timedelta
from faker import Faker
import random

fake = Faker()

# Constants for generating the data
NUM_VENDORS = 10
NUM_PERFORMANCE_RECORDS = 25
NUM_PURCHASE_ORDERS = 15

# Helper function to generate a random float
def random_float(low, high, precision=1):
    return round(random.uniform(low, high), precision)

# Generate vendor data
vendors = [
    {
        "model": "profile_management.vendor",
        "pk": i + 1,
        "fields": {
            "name": fake.company(),
            "contact_details": fake.company_email(),
            "address": fake.address(),
            "vendor_code": f"VENDOR-{i+1:03}",
            "on_time_delivery_rate": random_float(90.0, 100.0, 1),
            "quality_rating_avg": random_float(3.0, 5.0, 1),
            "average_response_time": random_float(5.0, 30.0, 1),  # in minutes/hours
            "fulfillment_rate": random_float(85.0, 100.0, 1)
        }
    } for i in range(NUM_VENDORS)
]

# Generate vendor performance records
vendor_performance_records = [
    {
        "model": "performance_evaluation.vendorperformancerecord",
        "pk": i + 1,
        "fields": {
            "vendor": (i % NUM_VENDORS) + 1,
            "date": (datetime.now() - timedelta(days=(i * 20))).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "on_time_delivery_rate": random_float(80.0, 100.0, 1),
            "quality_rating_avg": random_float(3.0, 5.0, 1),
            "average_response_time": random_float(5.0, 20.0, 1),  # in minutes/hours
            "fulfillment_rate": random_float(70.0, 100.0, 1)
        }
    } for i in range(NUM_PERFORMANCE_RECORDS)
]

# Generate purchase orders
purchase_orders = [
    {
        "model": "purchase_order_tracking.purchaseorder",
        "pk": i + 1,
        "fields": {
            "po_number": f"PO-{i+10001}",
            "vendor": (i % NUM_VENDORS) + 1,
            "order_date": (datetime.now() - timedelta(days=(i * 25 + 5))).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "delivery_date": (datetime.now() - timedelta(days=(i * 20))).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "items": [
                {"item_name": "Widget", "quantity": random.randint(1, 20), "unit_price": random_float(10.0, 50.0)},
                {"item_name": "Gadget", "quantity": random.randint(1, 30), "unit_price": random_float(15.0, 60.0)}
            ],
            "quantity": random.randint(10, 100),
            "status": random.choice(["PENDING", "COMPLETED", "CANCELLED"]),
            "quality_rating": random_float(3.0, 5.0, 1),
            "issue_date": (datetime.now() - timedelta(days=(i * 30 + 10))).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "acknowledgment_date": (datetime.now() - timedelta(days=(i * 25 + 12))).strftime("%Y-%m-%dT%H:%M:%SZ")
        }
    } for i in range(NUM_PURCHASE_ORDERS)
]

# Combine all data into one JSON structure
data = vendors + vendor_performance_records + purchase_orders

# Write to a JSON file
with open('sample_data.json', 'w') as file:
    json.dump(data, file, indent=4)
