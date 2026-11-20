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


class Car(models.Model):
    model = models.CharField(
        max_length=20,
    )

    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2000),
        ]
    )

    manufacturer = models.ForeignKey(
        to='Manufacturer',
        on_delete=models.CASCADE,
        related_name='cars',
    )

