# api/serializers.py

from rest_framework import serializers
from .models import Vehicle, TaxRule

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type']

class TaxRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxRule
        fields = ['city', 'start_time', 'end_time', 'amount']

class TaxCalculationSerializer(serializers.Serializer):
    vehicle_type = serializers.ChoiceField(choices=Vehicle.VEHICLE_TYPES)
    dates = serializers.ListField(child=serializers.DateTimeField())
    city = serializers.CharField(max_length=100)
