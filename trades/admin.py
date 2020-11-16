from django.contrib import admin
from trades.models import Deal, Pair, Provider
# Register your models here.


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'pair', 'quantity')
    search_fields = ['pair', 'quantity']


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'time', 'provider')
    search_fields = ['name', 'time', 'provider', 'time']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']