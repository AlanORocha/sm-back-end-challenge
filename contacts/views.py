from rest_framework import viewsets
from .models import Contato, ContatoSerializerv1, ContatoSerializerv2
from django_filters.rest_framework import DjangoFilterBackend


class ContatoViewSetv1(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializerv1
    # Filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']  


class ContatoViewsetv2(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializerv2
    # Filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']  
