from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User
from pessoais.models import Despesa
from django.http import HttpResponse

def despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    return render(request, 'usuarios/dashboard.html', {'despesa' : despesa})

def cadastrar_despesa(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        categoria =request.POST['categoria']
        valor = request.POST['valor']
        forma = request.POST['forma']
        data = request.POST['data']
        #pago = request.POST['pago']
        user = get_object_or_404(User, pk=request.user.id)
        despesa = Despesa.objects.create(pessoa=user, descricao=descricao, categoria=categoria, valor=valor, forma=forma, data=data)
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
    despesa_a_editar = {'despesa' : despesa}
    return render(request, 'pessoais/editar_despesa.html', despesa_a_editar)

def atualizar_despesa(request):
    if request.method == 'POST':
        despesa_id = request.POST['despesa_id']
        r = Despesa.objects.get(pk=despesa_id)
        r.descricao = request.POST['descricao']
        r.categoria =request.POST['categoria']
        r.valor = request.POST['valor']
        r.forma = request.POST['forma']
        r.data = request.POST['data']
        #pago = request.POST['pago']
        r.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/dashboard.html')
