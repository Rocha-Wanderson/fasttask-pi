from django.db import models
# Importa o modelo de User padrão do Django que já foi criado
from django.contrib.auth.models import User

# Opções de escolha para os campos (deixa o formulário mais fácil)
STATUS_OPCOES = [
    ('Pendente', 'Pendente'),
    ('Em Andamento', 'Em Andamento'),
    ('Concluída', 'Concluída'),
]

PRIORIDADE_OPCOES = [
    ('Baixa', 'Baixa'),
    ('Média', 'Média'),
    ('Alta', 'Alta'),
]

# Este é o nosso "molde" para a Tabela de Tarefas
# Baseado 100% no que planejamos e no feedback da Fast Line
class Tarefa(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_OPCOES,
        default='Pendente' # O padrão será "Pendente"
    )
    
    prioridade = models.CharField(
        max_length=20,
        choices=PRIORIDADE_OPCOES,
        default='Média' # O padrão será "Média"
    )
    
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_limite = models.DateField(blank=True, null=True, verbose_name="Data Limite")

    # Aqui está a "mágica" da conexão:
    # Quem criou a tarefa?
    usuario_criador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, # Se o usuário for deletado, a tarefa não some
        null=True,
        blank=True,
        related_name="tarefas_criadas"
    )
    
    # Quem é o responsável pela tarefa?
    usuario_responsavel = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tarefas_responsaveis"
    )

    # Isso faz o painel de admin mostrar o título da tarefa
    def __str__(self):
        return self.titulo