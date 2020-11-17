from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Provider(models.Model):
    def __str__(self):
        return f'{self.name}'

    name = models.CharField(
        unique=True,
        max_length=64
    )


class Pair(models.Model):
    def __str__(self):
        return f'{self.name} - {self.price} from {self.provider}. Time: {self.time}'

    name = models.CharField(
        max_length=64
    )

    time = models.DateTimeField(
        unique=True,
        default=datetime.now
    )

    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
        max_length=32
    )

    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE
    )


class Deal(models.Model):
    def __str__(self):
        return f'{self.quantity} - {self.pair}'

    quantity = models.PositiveIntegerField(
    )

    pair = models.ForeignKey(
        to=Pair,
        on_delete=models.CASCADE
    )
