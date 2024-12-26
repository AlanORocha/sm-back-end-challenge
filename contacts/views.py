from rest_framework import viewsets
from rest_framework.response import Response
from .models import Contato, ContatoSerializerv1, ContatoSerializerv2
from tools.check_version import verify_version


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()

    def get_serializer_class(self):
        version = verify_version(self.request)
        if version == "v2":
            return ContatoSerializerv2
        return ContatoSerializerv1

    def list(self, request, *args, **kwargs):
        # Pega todos os objetos do banco
        queryset = self.filter_queryset(self.get_queryset())

        # Filtro por nome
        name = request.query_params.get("name")
        if name:
            queryset = queryset.filter(name=name)
        if len(queryset) == 0:
            queryset = self.filter_queryset(self.get_queryset())
            queryset = queryset.filter(name__icontains=name)

        # Cria a paginação
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
