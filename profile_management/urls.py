from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet

router = DefaultRouter()
router.register(r"vendors", VendorViewSet, basename="vendor")

urlpatterns = [
    path(
        "vendors/<int:vendor_id>/",
        VendorViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="vendor-detail",
    ),
]

# Include the router URLs
urlpatterns += router.urls
