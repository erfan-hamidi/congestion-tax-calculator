# api/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import TaxRule

class CongestionTaxCalculatorTest(TestCase):
    def test_calculate_tax(self):
        # Scenario 1
        data1 = {
            "vehicle_type": "Car",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response1 = self.client.post('/api/vehicles/calculate_tax/', data1, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response1.data)
        self.assertEqual(response1.data['tax'], 16)  # 8 SEK (06:20:27) + 8 SEK (14:35:00)

        # Scenario 2
        data2 = {
            "vehicle_type": "Car",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T06:45:00"
            ],
            "city": "x"
        }
        response2 = self.client.post('/api/vehicles/calculate_tax/', data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response2.data)
        self.assertEqual(response2.data['tax'], 13)  # 13 SEK (06:45:00) since it's within the same hour

        # Scenario 3
        data3 = {
            "vehicle_type": "Car",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T07:15:00"
            ],
            "city": "x"
        }
        response3 = self.client.post('/api/vehicles/calculate_tax/', data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response3.data)
        self.assertEqual(response3.data['tax'], 18)  # 8 SEK (06:20:27) + 18 SEK (07:15:00)

        # Scenario 4: Maximum daily tax cap
        data4 = {
            "vehicle_type": "Car",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T07:15:00",
                "2013-02-08T08:00:00",
                "2013-02-08T15:45:00",
                "2013-02-08T16:30:00",
                "2013-02-08T17:45:00"
            ],
            "city": "x"
        }
        response4 = self.client.post('/api/vehicles/calculate_tax/', data4, format='json')
        self.assertEqual(response4.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response4.data)
        self.assertEqual(response4.data['tax'], 60)  # Maximum tax per day is 60 SEK

        # Scenario 5: No tax for free vehicles (e.g., Emergency)
        data5 = {
            "vehicle_type": "Emergency",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response5 = self.client.post('/api/vehicles/calculate_tax/', data5, format='json')
        self.assertEqual(response5.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response5.data)
        self.assertEqual(response5.data['tax'], 0)  # Emergency vehicles are toll-free


    def test_calculate_tax_for_other_vehicles(self):
        # Scenario 1: Motorbike (tax-free)
        data1 = {
            "vehicle_type": "Motorbike",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response1 = self.client.post('/api/vehicles/calculate_tax/', data1, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response1.data)
        self.assertEqual(response1.data['tax'], 0)  # Motorbikes are toll-free

        # Scenario 2: Diplomat (tax-free)
        data2 = {
            "vehicle_type": "Diplomat",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response2 = self.client.post('/api/vehicles/calculate_tax/', data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response2.data)
        self.assertEqual(response2.data['tax'], 0)  # Diplomat vehicles are toll-free

        # Scenario 3: Tractor (tax-free)
        data3 = {
            "vehicle_type": "Tractor",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response3 = self.client.post('/api/vehicles/calculate_tax/', data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response3.data)
        self.assertEqual(response3.data['tax'], 0)  # Tractors are toll-free

        # Scenario 4: Foreign vehicle (tax-free)
        data4 = {
            "vehicle_type": "Foreign",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response4 = self.client.post('/api/vehicles/calculate_tax/', data4, format='json')
        self.assertEqual(response4.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response4.data)
        self.assertEqual(response4.data['tax'], 0)  # Foreign vehicles are toll-free

        # Scenario 5: Military vehicle (tax-free)
        data5 = {
            "vehicle_type": "Military",
            "dates": [
                "2013-02-08T06:20:27",
                "2013-02-08T14:35:00"
            ],
            "city": "x"
        }
        response5 = self.client.post('/api/vehicles/calculate_tax/', data5, format='json')
        self.assertEqual(response5.status_code, status.HTTP_200_OK)
        self.assertIn('tax', response5.data)
        self.assertEqual(response5.data['tax'], 0)  # Military vehicles are toll-free
