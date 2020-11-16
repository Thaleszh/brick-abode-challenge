from rest_framework.viewsets import ModelViewSet

from trades.models import Deal, Pair, Provider
import trades.serializers as serializer
# Create your views here.


class DealViewSet(ModelViewSet):
    queryset = Deal.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadDealSerializer
        return serializer.CreateDealSerializer


class PairViewSet(ModelViewSet):
    queryset = Pair.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadPairSerializer
        return serializer.CreatePairSerializer


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = serializer.ProviderSerializer
