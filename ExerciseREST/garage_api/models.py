from decimal import Decimal
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


class Part(models.Model):
    name = models.CharField(
        max_length=20,
    )

    serial_number = models.CharField(
        max_length=20,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
        ]
    )

    manufacturer = models.ForeignKey(
        to='Manufacturer',
        on_delete=models.CASCADE,
        related_name='parts',
    )

    cars = models.ManyToManyField(
        to='Car',
        related_name='parts',
    )
