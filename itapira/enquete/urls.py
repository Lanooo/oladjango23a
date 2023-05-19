from django.contrib import admin
from django.urls import path, include

from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musica', views.caneta, name='caneta'),
     # ex: /enquete/5
    path("<int:questao_id>/", views.detalhe, name="detalhes"),
     # ex: /enquete/5/resultados
    path("<int:questao_id>/resultados/", views.resultados, name="resultados"),
     # ex: /enquete/5/voto
    path("<int:questao_id>/voto/", views.voto, name="voto"),
]