# urls.py
from django.urls import path
from .views import SalesSummaryAPIView

urlpatterns = [
    path('sales-summary/', SalesSummaryAPIView.as_view(), name='sales-summary'),
]
