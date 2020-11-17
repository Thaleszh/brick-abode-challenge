import datetime

from trades.models import Pair, Provider, Deal

import warnings
warnings.filterwarnings("ignore")

print("List of Providers:")
for provider in Provider.objects.all():
    print(provider)
print()

print("List of Pairs:")
for pair in Pair.objects.all():
    print(pair)
print()

print("List of deals made before 17 Nov:")
for deal in Deal.objects.filter(pair__time__lt=datetime.date(2020, 11, 17)):
    print(deal)
print()

print("List of deals with quantities over 1000")
for deal in Deal.objects.filter(quantity__gt=1000):
    print(deal)
print()

print("List of deals made from Nemesis")
for deal in Deal.objects.filter(pair__provider__name="Nemesis"):
    print(deal)
print()
