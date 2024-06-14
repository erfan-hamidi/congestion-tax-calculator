# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, TaxRuleViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'taxrules', TaxRuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
