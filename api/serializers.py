from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from api.models import *


class CimetiereFoLocSerializer(ModelSerializer):
    class Meta:
        model = Cimetiere
        fields = ['id', 'nom_cimetiere', 'superficie', 'categorie']


class LocaliteSerializer(ModelSerializer):
    cimetieres = CimetiereFoLocSerializer(many=True, read_only=True,)

    class Meta:
        model = Localite
        fields = ['id', 'nom_localite', 'superficie', 'description', 'cimetieres']

class LocaliteForDefSerializer(ModelSerializer):

    class Meta:
        model = Localite
        fields = ['id', 'nom_localite', 'superficie', 'description']


class CategorieCimetiereSerializer(ModelSerializer):
    class Meta:
        model = CategorieCimetiere
        fields = ['id', 'nom_categorie', 'description']


class TombeForCimSerializer(ModelSerializer):
    defunt = serializers.IntegerField(write_only=True)

    class Meta:
        model = Tombe
        fields = ['id', 'numero_tombe', 'lat', 'lon', 'defunt']


class CimetiereSerializer(ModelSerializer):
    tombes = TombeForCimSerializer(many=True, read_only=True)

    class Meta:
        model = Cimetiere
        fields = ['id', 'nom_cimetiere', 'superficie', 'categorie', 'localite', 'tombes']


class CimetiereForDefSerializer(ModelSerializer):
    localite = LocaliteForDefSerializer(many=False, read_only=True)
    class Meta:
        model = Cimetiere
        fields = ['id', 'nom_cimetiere', 'superficie', 'categorie', 'localite']


class TombeSerializer(ModelSerializer):
    defunt = serializers.IntegerField(write_only=True)
    cimetiere = serializers.IntegerField(write_only=True)

    class Meta:
        model = Tombe
        fields = ['id', 'numero_tombe', 'lat', 'lon', 'cimetiere', 'defunt']


class TombeForDefSerializer(ModelSerializer):
    defunt = serializers.IntegerField(write_only=True)
    cimetiere = CimetiereForDefSerializer(many=False, read_only=True)

    class Meta:
        model = Tombe
        fields = ['id', 'numero_tombe', 'lat', 'lon', 'cimetiere', 'defunt']


class ExhumationSerializer(ModelSerializer):
    defunt = serializers.IntegerField(write_only=True)

    class Meta:
        model = Exhumation
        fields = ['id', 'date_exhumation', 'last_cimetiere',
                  'new_cimetiere', 'defunt']


class DefunSerializer(ModelSerializer):
    tombe = TombeForDefSerializer(many=False, read_only=True)
    exhumations = ExhumationSerializer(many=True, read_only=True)

    class Meta:
        model = Defunt
        fields = ['id', 'matricule', 'nom', 'prenom', 'genre', 'nationalite', 'date_naiss',
                  'date_deces', 'date_inhumation', 'statut', 'tombe', 'exhumations']
