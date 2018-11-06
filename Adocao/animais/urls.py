from django.urls import path

# importa tudo que tem no views.py do app "animais"
from .views import *
# . indica para o python buscar o views dentro deste diretório
# * indica para importar tudo de lá

urlpatterns = [
    #   ( endereço, método da view, nome da url )
    path('', Index.as_view(), name="index" ),
    path('ajuda/', Ajuda.as_view(), name="ajuda"),
    path('contato/', Contato.as_view(), name="contato"),
    path('pagina_inicial/', Inicio.as_view(), name="pagina_inicial")
]
