from django.contrib import admin
from contacts.models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    fieldsets = [  # ORDENA OS CAMPOS DOS FORMS
        (
            "Informações do Contato",
            {"fields": ["name", "cellular", "email", "region"]},
        )
    ]

    list_display = (  # EXIBIÇÃO DAS VARIÁVEIS NA LISTA DE CONTATOS
        "id",
        "name",
        "cellular",
        "email",
        "region"
    )

    search_fields = ("id", "cellular", "name", "email", "region")
