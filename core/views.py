from django.shortcuts import render, redirect  # 1. IMPORTAMOS O 'redirect'
from .models import Tarefa
from django.contrib.auth.models import User  # 2. IMPORTAMOS O "User" PADRÃO DO DJANGO

# Esta é a nossa View "turbinada"
def dashboard(request):
    
    # 2. LÓGICA DE CONTAGEM:
    total_pendente = Tarefa.objects.filter(status='Pendente').count()
    total_andamento = Tarefa.objects.filter(status='Em Andamento').count()
    total_concluida = Tarefa.objects.filter(status='Concluída').count()
    
    # 3. CRIAMOS O "CONTEXTO" PARA ENVIAR AO HTML:
    contexto = {
        'pendentes': total_pendente,
        'andamento': total_andamento,
        'concluidas': total_concluida,
    }
    
    # 4. Renderizamos o HTML, agora enviando o "contexto" junto
    return render(request, 'dashboard.html', contexto)

#
# ESTA É A FUNÇÃO QUE ATUALIZAMOS:
#
def adicionar_tarefa(request):
    
    # --- LÓGICA DE SALVAR (POST) ---
    # Se o usuário clicou no botão "SALVAR" (enviou o formulário)
    if request.method == 'POST':
        # 1. Pegamos os dados do formulário
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        prioridade = request.POST.get('prioridade')
        data_limite = request.POST.get('data_limite')
        observacoes = request.POST.get('observacoes')
        responsavel_id = request.POST.get('responsavel') # Pega o ID (ex: "3")

        # 2. Buscamos os objetos de Usuário no banco
        try:
            usuario_responsavel = User.objects.get(id=responsavel_id)
        except User.DoesNotExist:
            usuario_responsavel = None # Se não encontrar, deixa nulo

        # 3. Criamos a nova Tarefa no banco
        nova_tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            status=status,
            prioridade=prioridade,
            observacoes=observacoes,
            usuario_responsavel=usuario_responsavel
            # (Vamos lidar com 'usuario_criador' quando fizermos o login)
        )
        
        # 4. Trata a data (se ela não for preenchida, vem vazia)
        if data_limite:
            nova_tarefa.data_limite = data_limite
        
        # 5. Salva no banco de dados XAMPP
        nova_tarefa.save()
        
        # 6. Redireciona o usuário de volta para o Dashboard
        return redirect('dashboard') # Usa o "name='dashboard'" do nosso urls.py

    # --- LÓGICA DE MOSTRAR A PÁGINA (GET) ---
    # Se o usuário apenas "pediu" para ver a página
    else:
        # Buscamos todos os usuários cadastrados no Admin
        todos_usuarios = User.objects.all()
        contexto = {
            'usuarios_da_fastline': todos_usuarios # Envia a lista para o HTML
        } 
        return render(request, 'adicionar_tarefa.html', contexto)
    # ... (as funções dashboard e adicionar_tarefa ficam aqui em cima) ...

# Esta é a nossa nova "View" para a página da lista de tarefas
def minhas_tarefas(request):
    
    # 1. LÓGICA DE BUSCA:
    # Buscamos TODOS os objetos "Tarefa" no banco
    # e ordenamos pelas mais novas primeiro (usando '-data_criacao')
    todas_as_tarefas = Tarefa.objects.all().order_by('-data_criacao')

    # 2. CRIAMOS O "CONTEXTO" PARA ENVIAR AO HTML:
    contexto = {
        'lista_de_tarefas': todas_as_tarefas, # Envia a lista completa
    }
    
    # 3. Renderizamos o HTML, enviando o "contexto" junto
    return render(request, 'minhas_tarefas.html', contexto)