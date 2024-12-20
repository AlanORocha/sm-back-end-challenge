from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class Client(admin.ModelAdmin):
    fieldsets = [ # ORDENA OS CAMPOS DOS FORMS
        ('Informações do Cliente', {'fields': ['id','email', 'name', 'cellular', 'passwd', 'document', 'cep', 'residence', 'timezone']})
    ]

    list_display = ( # EXIBIÇÃO DAS VARIÁVEIS NA LISTA DE CLIENTES TOTAIS
        'id',
        'email',
        'name',
        'cellular',
        'passwd',
        'document',
        'cep',
        'residence',
        'timezone'
        )

    search_fields = (
        'id',
        'cellular',
        'name'
        )