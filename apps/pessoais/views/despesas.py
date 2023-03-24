from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User
from pessoais.models import Despesa
from pessoais.forms import DespesasForm

def despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    return render(request, 'usuarios/dashboard.html', {'despesa' : despesa})

def cadastrar_despesa(request):
    form = DespesasForm()
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            descricao = request.POST['descricao']
            categoria =request.POST['categoria']
            valor = request.POST['valor']
            forma = request.POST['forma']
            data = request.POST['data']
            estado = request.POST['estado']
            user = get_object_or_404(User, pk=request.user.id)
            despesa = Despesa.objects.create(pessoa=user, descricao=descricao, categoria=categoria, valor=valor, forma=forma, data=data, estado=estado)
            despesa.save()
            return redirect('dashboard')
    else:
        return render(request, 'usuarios/dashboard.html')

def apagar_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    despesa.delete()
    return redirect('dashboard')

def editar_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    formD = DespesasForm(instance = despesa)
    despesa_a_editar = {'formD': formD}
    return render(request, 'pessoais/editar_despesa.html', despesa_a_editar)

def atualizar_despesa(request):
    form = DespesasForm()
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            descricao = request.POST['descricao']
            categoria =request.POST['categoria']
            valor = request.POST['valor']
            forma = request.POST['forma']
            data = request.POST['data']
            estado = request.POST['estado']
            user = get_object_or_404(User, pk=request.user.id)
            despesa = Despesa.objects.create(pessoa=user, descricao=descricao, categoria=categoria, valor=valor, forma=forma, data=data, estado=estado)
            despesa.save()
            return redirect('dashboard')
    else:
        return render(request, 'usuarios/dashboard.html')
