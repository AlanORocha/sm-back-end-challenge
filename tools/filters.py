from django_filters import rest_framework as filters
from contacts.models import Contato


class ContatoFilter(filters.FilterSet):
    # Filtro para buscar contatos pelo nome
    name = filters.CharFilter(field_name="name")

    class Meta:
        model = Contato
        fields = ["name"]
