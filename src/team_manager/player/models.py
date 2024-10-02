from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Player(models.Model):
    DOMINANT_HAND = [
        ("R", "RIGHT"),
        ("L", "LEFT"),
        ("A", "AMBIDEXTROUS")
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    contact_phone = PhoneNumberField()
    height = models.DecimalField(max_digits=8, decimal_places=4)
    weight = models.DecimalField(max_digits=8, decimal_places=4)
    dominant_hand = models.CharField(max_length=10, choices=DOMINANT_HAND)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'