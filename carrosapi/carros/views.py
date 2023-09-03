from rest_framework import generics
from .models import Carro, Fabricante
from .serializers import CarroSerializer, FabricanteSerializer

class CarroListCreateView(generics.ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class FabricanteListCreateView(generics.ListCreateAPIView):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
