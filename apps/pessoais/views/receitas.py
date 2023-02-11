from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from pessoais.models import Receita

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'usuarios/dashboard.html', {'receita' : receita})

def cadastrar_receita(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        categoria =request.POST['categoria']
        valor = request.POST['valor']
        forma = request.POST['forma']
        data = request.POST['data']
        #pago = request.POST['pago']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, descricao=descricao, categoria=categoria, valor=valor, forma=forma, data=data)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/dashboard.html')

def apagar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita' : receita}
    return render(request, 'pessoais/editar_receita.html', receita_a_editar)

def atualizar_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
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
