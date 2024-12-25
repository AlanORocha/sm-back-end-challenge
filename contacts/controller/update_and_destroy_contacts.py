from rest_framework import generics
from contacts.models import Contato, ContatoSerializerv1, ContatoSerializerv2
from tools.check_version import verify_version


# Recuperar, Atualizar e Excluir Contatos
class ContatoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()

    # Usar um serializador específico dependendo da versão da API
    def get_serializer_class(self):
        version = verify_version(self.request)
        if version == "v2":
            return ContatoSerializerv2
        return ContatoSerializerv1
