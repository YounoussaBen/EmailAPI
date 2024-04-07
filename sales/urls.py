from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesSummaryViewSet

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'sales-summary', SalesSummaryViewSet, basename='sales-summary')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
