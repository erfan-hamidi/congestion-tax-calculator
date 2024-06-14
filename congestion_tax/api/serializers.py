# calculator/serializers.py

from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type']

class TaxCalculationSerializer(serializers.Serializer):
    vehicle_type = serializers.ChoiceField(choices=Vehicle.VEHICLE_TYPES)
    dates = serializers.ListField(child=serializers.DateTimeField())
