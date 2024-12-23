from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContatoViewSetv1, ContatoViewsetv2

# Router para a versão 1
router = DefaultRouter()
router.register(r"contatos", ContatoViewSetv1, basename="contatos-v1")

# Router para a versão 2
router_v2 = DefaultRouter()
router_v2.register(r'contatos', ContatoViewsetv2, basename='contatos-v2')


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v2/", include(router_v2.urls))
    ]
