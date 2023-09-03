from rest_framework import serializers
from .models import Carro, Fabricante

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'
