from django.db import models


class TaxRule(models.Model):
    city = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.city}: {self.start_time} - {self.end_time} ({self.amount} SEK)"

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Car', 'Car'),
        ('Motorbike', 'Motorbike'),
        ('Tractor', 'Tractor'),
        ('Emergency', 'Emergency'),
        ('Diplomat', 'Diplomat'),
        ('Foreign', 'Foreign'),
        ('Military', 'Military'),
    )

    vehicle_type = models.CharField(max_length=100, choices=VEHICLE_TYPES)

    def __str__(self):
        return self.vehicle_type
    
class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vehicle_type = "Car"

class Motorbike(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vehicle_type = "Motorbike"


