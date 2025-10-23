from django.contrib import admin
from .models import Tarefa  # Importa o "molde" da Tarefa que criamos

# Classe para customizar como as Tarefas aparecem no Admin
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prioridade', 'usuario_responsavel', 'data_limite')
    list_filter = ('status', 'prioridade', 'usuario_responsavel')
    search_fields = ('titulo', 'descricao')

# "Registre" a tabela Tarefa no site de admin, usando a customização acima
admin.site.register(Tarefa, TarefaAdmin)