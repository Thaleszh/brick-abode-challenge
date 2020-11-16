from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from trades.views import ProviderViewSet, DealViewSet, PairViewSet

providersRouter = routers.DefaultRouter()
providersRouter.register(r'provider', ProviderViewSet)

pairRouter = routers.DefaultRouter()
pairRouter.register(r'pair', PairViewSet)

dealRouter = routers.DefaultRouter()
dealRouter.register(r'deal', DealViewSet)

urlpatterns = [
    url(r'^', include(providersRouter.urls)),
    url(r'^', include(dealRouter.urls)),
    url(r'^', include(pairRouter.urls)),
]
