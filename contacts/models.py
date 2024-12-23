from django.db import models
from rest_framework import serializers
import uuid


# Modelo que representa a entidade de um contato
class Contato(models.Model):
    # ID do contato - Criado automaticamente
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    # Informações preenchidas no cadastro
    # Nome do contato
    name = models.CharField(max_length=255, verbose_name="Nome do Contato")

    # Telefone do contato
    cellular = models.CharField(
        max_length=25, verbose_name="Telefone", help_text="Padrão: +5511012345678"
    )

    # Email do contato
    email = models.CharField(
        max_length=255, verbose_name="Email", blank=True, null=True
    )

    # Região do contato - Ex: BR
    region = models.CharField(
        max_length=3, verbose_name="Região", blank=True, null=True
    )

    def __str__(self):
        return self.name


# Serializador do modelo Contato - Versão 1
class ContatoSerializerv1(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ["id", "name", "cellular"]


# Serializador do modelo Contato - Versão 2
class ContatoSerializerv2(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ["id", "name", "cellular", "email", "region"]
