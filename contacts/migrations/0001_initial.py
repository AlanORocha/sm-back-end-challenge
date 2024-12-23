# Generated by Django 5.1.4 on 2024-12-23 12:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contato",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Nome do Contato"),
                ),
                (
                    "cellular",
                    models.CharField(
                        help_text="Padrão: +5511012345678",
                        max_length=25,
                        verbose_name="Telefone",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        blank=True, max_length=3, null=True, verbose_name="Região"
                    ),
                ),
            ],
        ),
    ]
