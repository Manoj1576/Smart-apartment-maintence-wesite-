from django.db import models

# Create your models here.

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    electricity = models.DecimalField(max_digits=10, decimal_places=2)
    water = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    parking = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number}"
