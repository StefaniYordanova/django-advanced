from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(
        max_length=20,
    )

    country = models.CharField(
        max_length=10,
    )

    founded_year = models.PositiveIntegerField()


class Car(models.Model):
    model = models.CharField(
        max_length=20,
    )

    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
        ]
    )

    manufacturer = models.ForeignKey(
        to='Manufacturer',
        on_delete=models.CASCADE,
        related_name='cars',
    )

