from datetime import datetime
from django.db import models


# Create your models here.
class Provider(models.Model):
    def __str__(self):
        return f'{self.name}'

    name = models.CharField(
        max_length=64
    )


class Pair(models.Model):
    def __str__(self):
        return f'{self.name} - {self.price} from {self.provider}. Time: {self.time}'

    name = models.CharField(
        max_length=64
    )

    time = models.DateTimeField(
        default=datetime.now
    )

    price = models.FloatField(
        max_length=32
    )

    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE
    )


class Deal(models.Model):
    def __str__(self):
        return f'{self.quantity} - {self.pair}'

    quantity = models.IntegerField(
    )

    pair = models.ForeignKey(
        to=Pair,
        on_delete=models.CASCADE
    )
