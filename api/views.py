from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from api.serializers import *


# Create your views here.
class LocaliteModelViewSet(ModelViewSet):
    serializer_class = LocaliteSerializer
    queryset = Localite.objects.filter()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom_localite']


class CategorieCimetiereModelViewSet(ModelViewSet):
    serializer_class = CategorieCimetiereSerializer
    queryset = CategorieCimetiere.objects.filter()


class CimetiereModelViewSet(ModelViewSet):
    serializer_class = CimetiereSerializer
    queryset = Cimetiere.objects.filter()


class DefuntModelViewSet(ModelViewSet):
    serializer_class = DefunSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['matricule', 'nom', 'prenom',]
    filterset_fields = ['date_deces', 'date_inhumation', 'statut']

    def get_queryset(self):
        return  Defunt.objects.filter(statut=True)

class TombeModelViewSet(ModelViewSet):
    serializer_class = TombeSerializer
    queryset = Tombe.objects.filter()
