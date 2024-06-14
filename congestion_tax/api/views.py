# api/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vehicle, TaxRule
from .serializers import VehicleSerializer, TaxRuleSerializer, TaxCalculationSerializer
from .utils import calculate_congestion_tax

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=False, methods=['post'])
    def calculate_tax(self, request):
        serializer = TaxCalculationSerializer(data=request.data)
        if serializer.is_valid():
            vehicle_type = serializer.validated_data['vehicle_type']
            dates = serializer.validated_data['dates']

            vehicle = Vehicle(vehicle_type=vehicle_type)
            tax = calculate_congestion_tax(vehicle, dates)

            return Response({'tax': tax}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaxRuleViewSet(viewsets.ModelViewSet):
    queryset = TaxRule.objects.all()
    serializer_class = TaxRuleSerializer
