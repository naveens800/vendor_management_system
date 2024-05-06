# API Documentation.

##  VendorViewSet Overview

> The `VendorViewSet` class provides a set of API endpoints for managing vendor resources. This viewset allows clients to perform CRUD operations on vendor objects through a RESTful API. Below is a summary of the endpoints available and their functions.

## Endpoints

1. **POST /api/vendors/**
   - **Description:** Create a new vendor.
   - **Response:** Returns the created vendor's details.

2. **GET /api/vendors/**
   - **Description:** List all vendors.
   - **Response:** Returns a list of all vendors.

3. **GET /api/vendors/{vendor_id}/**
   - **Description:** Retrieve a specific vendor's details.
   - **Path Parameter:** `vendor_id` - The unique identifier of the vendor to retrieve.
   - **Response:** Returns the details of the specified vendor.

4. **PUT /api/vendors/{vendor_id}/**
   - **Description:** Update a vendor's details.
   - **Path Parameter:** `vendor_id` - The unique identifier of the vendor to update.
   - **Response:** Returns the updated vendor's details.

5. **DELETE /api/vendors/{vendor_id}/**
   - **Description:** Delete a vendor.
   - **Path Parameter:** `vendor_id` - The unique identifier of the vendor to delete.
   - **Response:** Returns an empty response with a `204 No Content` status.

## PurchaseOrderViewSet Overview
> The `PurchaseOrderViewSet` class provides a set of API endpoints for managing purchase orders. Clients can perform CRUD operations on purchase orders, as well as acknowledge them, using this RESTful API.

## Endpoints

1. **POST /api/purchase_orders/**
   - **Description:** Create a purchase order.
   - **Response:** Returns the created purchase order's details.

2. **GET /api/purchase_orders/**
   - **Description:** List all purchase orders. Optionally, clients can filter by vendor.
   - **Response:** Returns a list of all matching purchase orders.

3. **GET /api/purchase_orders/{po_id}/**
   - **Description:** Retrieve details of a specific purchase order.
   - **Path Parameter:** `po_id` - The unique identifier of the purchase order.
   - **Response:** Returns the details of the specified purchase order.

4. **PUT /api/purchase_orders/{po_id}/**
   - **Description:** Update a purchase order.
   - **Path Parameter:** `po_id` - The unique identifier of the purchase order to update.
   - **Response:** Returns the updated purchase order's details.

5. **DELETE /api/purchase_orders/{po_id}/**
   - **Description:** Delete a purchase order.
   - **Path Parameter:** `po_id` - The unique identifier of the purchase order to delete.
   - **Response:** Returns an empty response with a `204 No Content` status.

6. **POST /api/purchase_orders/{po_id}/acknowledge/**
   - **Description:** Acknowledge a specific purchase order, updating its `acknowledgment_date`.
   - **Path Parameter:** `po_id` - The unique identifier of the purchase order to acknowledge.
   - **Response:** Returns an empty response with a `200 OK` status if successful, otherwise `404 Not Found` if the purchase order doesn't exist.

## vendor_performance Overview

> The `vendor_performance` function provides an API endpoint to retrieve performance metrics for a specific vendor. The endpoint is designed to analyze and return various performance statistics that help in evaluating vendor quality.

## Endpoint

**GET /api/vendors/{vendor_id}/performance**

- **Description:** Retrieves performance metrics for a specific vendor.
- **Path Parameter:** `vendor_id` - The unique identifier of the vendor whose performance is being retrieved.
- **Response:** Returns a list of serialized performance data, which may include:
  - `on_time_delivery_rate`
  - `quality_rating_avg`
  - `average_response_time`
  - `fulfillment_rate`
