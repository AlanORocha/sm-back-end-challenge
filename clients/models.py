from django.db import models
import uuid
import pytz

# Modelo que representa a entidade de um cliente
class Client(models.Model):
    # ID do cliente - Criado automaticamente
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    # Informações preenchidas no cadastro
    email = models.CharField(
        max_length=255,
        verbose_name="E-mail",
        help_text="E-mail do Cliente",
        unique=True,
    )

    name = models.CharField(
        max_length=255, verbose_name="Razão Social"
    )
    cellular = models.CharField(
        max_length=25,
        verbose_name="Contato",
        help_text="Padrão: +5511123456789",
    )

    # Senha do Cliente
    passwd = models.CharField(max_length=255, verbose_name="password")

    # Informações adicionais não obrigatórias
    document = models.CharField(
        max_length=25,
        verbose_name="CPF/CNPJ do Cliente",
        help_text="CPF ou CNPJ do cliente",
        null=True,
        blank=True,
    )

    cep = models.CharField(
        max_length=8,
        verbose_name="CEP",
        help_text="CEP do Cliente",
        null=True,
        blank=True,
    )

    residence = models.CharField(
        max_length=5,
        verbose_name="Nº da Residência",
        help_text="Nº da Residência",
        null=True,
        blank=True,
    )

    # # Datas
    # Quando foi criado o cadastro
    created_at = models.DateTimeField(
        auto_now_add=True, 
        editable=False, 
        verbose_name="Criado em"
    )
    # Atualização mais recente do cadastro
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name="Atualizado em",
        blank=True,
        null=True,
    )


    # Fuso horário do cliente
    TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
    timezone = models.CharField(
        max_length=50, choices=TIMEZONE_CHOICES, default="America/Sao_Paulo"
    )


    class Meta:
        verbose_name_plural = "Clientes"
        db_table = "clients_client"