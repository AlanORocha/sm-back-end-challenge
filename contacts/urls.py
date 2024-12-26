from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContatoViewSet

# Cria um router para gerenciar automaticamente as rotas do ViewSet
router = DefaultRouter()
router.register(
    r"contatos", ContatoViewSet, basename="contato"
)  # Coloca o nome como 'contato' para manuseamento mais simples

urlpatterns = [
    path("v1/", include(router.urls)),  # Rotas para versão 1
    path("v2/", include(router.urls)),  # Rotas para versão 2
]
