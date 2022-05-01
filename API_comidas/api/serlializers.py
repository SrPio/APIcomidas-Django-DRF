from django.db.models import fields
from rest_framework import serializers
from .models import Alimento, Plato
from drf_writable_nested import WritableNestedModelSerializer


class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = ['nombre', 'categoria',]

class PlatoSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    alimento = AlimentoSerializer(many=True)
    class Meta:
        model = Plato
        fields = ['nombre', 'tiempo', 'categoria', 'alimento']
        depth = 1