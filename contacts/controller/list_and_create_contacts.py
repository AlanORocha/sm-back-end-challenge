from rest_framework import generics
from contacts.models import Contato, ContatoSerializerv1, ContatoSerializerv2
from django_filters.rest_framework import DjangoFilterBackend
from tools.filters import ContatoFilter
from tools.check_version import verify_version


# Listar e Criar Contatos
class ContatoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContatoFilter

    # Usar um serializador específico dependendo da versão da API
    def get_serializer_class(self):
        version = verify_version(self.request)
        if version == "v2":
            return ContatoSerializerv2
        return ContatoSerializerv1
