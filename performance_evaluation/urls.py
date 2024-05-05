from django.urls import path, include
from rest_framework.routers import DefaultRouter
from performance_evaluation import views


urlpatterns = [
    path('vendors/<str:vendor_id>/performance:', views.vendor_performance, name='vendor-performance'),
]
