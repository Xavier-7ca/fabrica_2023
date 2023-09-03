from django.urls import path
from .views import CarroListCreateView, FabricanteListCreateView

urlpatterns = [
    path('carros/', CarroListCreateView.as_view(), name='carro-list-create'),
    path('fabricantes/', FabricanteListCreateView.as_view(), name='fabricante-list-create'),
]
