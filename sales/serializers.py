# serializers.py
from rest_framework import serializers
from .models import SalesSummary

class SalesSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesSummary
        fields = '__all__'
        extra_kwargs = {field: {'required': False} for field in fields}