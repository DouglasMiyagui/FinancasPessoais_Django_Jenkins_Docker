from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from pessoais.models import Receita
from pessoais.forms import ReceitasForm

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'usuarios/dashboard.html', {'receita' : receita})

def cadastrar_receita(request):
    """Função que cadastra a receita, redireciona para a url dashboard que retorna a página dashboard.html"""
    form = ReceitasForm()
    if request.method == 'POST':
        form = ReceitasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            descricao = request.POST['descricao']
            categoria =request.POST['categoria']
            valor = request.POST['valor']
            forma = request.POST['forma']
            data = request.POST['data']
            pago = request.POST['pago']
            user = get_object_or_404(User, pk=request.user.id)
            receita = Receita.objects.create(pessoa=user, descricao=descricao, categoria=categoria, valor=valor, forma=forma, data=data, pago=pago)
            receita.save()
            
            return redirect('dashboard')
    else:
        return render(request, 'usuarios/dashboard.html')

def apagar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):
    """Função que pega a receita pelo id e carrega no formulário para editar na página editar_receita.html"""
    receita = get_object_or_404(Receita, pk=receita_id)
    formR = ReceitasForm(instance = receita)
    receita_a_editar = {'formR': formR}
    return render(request, 'pessoais/editar_receita.html', receita_a_editar)

def atualizar_receita(request):
    """Função que recebe do formulário a receita editada, atualiza os dados gravando no banco de dados e redireciona para a url dashboard"""
    form = ReceitasForm()
    if request.method == 'POST':
        form = ReceitasForm(request.POST)
        if form.is_valid():
            descricao = request.POST['descricao']
            categoria =request.POST['categoria']
            valor = request.POST['valor']
            forma = request.POST['forma']
            data = request.POST['data']
            pago = request.POST['pago']
            user = get_object_or_404(User, pk=request.user.id)
            receita = Receita.objects.create(pessoa=user, descricao=descricao, categoria=categoria, valor=valor, forma=forma, data=data, pago=pago)
            receita.save()
            return redirect('dashboard')
    else:
        return render(request, 'usuarios/dashboard.html')
