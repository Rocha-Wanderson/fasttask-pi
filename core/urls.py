from django.urls import path
from . import views  # Importa o views.py da nossa pasta 'core'

urlpatterns = [
    # Quando o endereço for "vazio" (''), chame a view "dashboard"
    # Damos a ela o nome de 'dashboard' para referência interna
    path('', views.dashboard, name='dashboard'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('minhas-tarefas/', views.minhas_tarefas, name='minhas_tarefas'),
]