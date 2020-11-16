from django.db import models


# Create your models here.
class Provider(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=64
    )


class User(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=64
    )


class Pair(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=64
    )

    time = models.DateTimeField

    price = models.FloatField(
        max_length=32
    )

    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE
    )


class Deal(models.Model):
    def __str__(self):
        return self.pair.__str__() + 'x' + self.quantity

    quantity = models.ImageField(
        max_length=32
    )

    pair = models.ForeignKey(
        to=Pair,
        on_delete=models.CASCADE
    )
