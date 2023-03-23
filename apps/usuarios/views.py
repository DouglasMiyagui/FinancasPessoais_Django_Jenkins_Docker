from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from pessoais.models import Receita, Despesa
from pessoais.forms import ReceitasForm, DespesasForm



def cadastrar_usuario(request):
    """ cadastra uma pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastrar_usuario')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastrar_usuario')
        if senhas_diferentes(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastrar_usuario')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastrar_usuario')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastrar_usuario')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso.')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastrar_usuario.html')

def login(request):
    """ Realiza o login de uma pessoa no sistema """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """ APP individual do usuario logado no sistema """

    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.all().order_by('data').filter(pessoa=id, status=1)
        despesas = Despesa.objects.all().order_by('data').filter(pessoa=id, status=1)
        formR = ReceitasForm()
        formD = DespesasForm()
        dados = {'receitas': receitas, 'despesas': despesas, 'formR': formR, 'formD': formD}
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def senhas_diferentes(senha, senha2):
    return senha != senha2
