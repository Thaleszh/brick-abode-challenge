from rest_framework.serializers import ModelSerializer

from trades.models import Pair, Deal, Provider


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ['__all__']


class CreatePairSerializer(ModelSerializer):
    class Meta:
        model = Pair
        fields = ['id', 'name', 'price', 'time', 'provider']


class ReadPairSerializer(ModelSerializer):
    provider = ProviderSerializer()

    class Meta:
        model = Pair
        fields = ['id', 'name', 'price', 'time', 'provider']


class CreateDealSerializer(ModelSerializer):
    class Meta:
        model = Deal
        fields = ['id', 'quantity', 'pair']


class ReadDealSerializer(ModelSerializer):
    pair = ReadPairSerializer()

    class Meta:
        model = Deal
        fields = ['id', 'quantity', 'pair']
