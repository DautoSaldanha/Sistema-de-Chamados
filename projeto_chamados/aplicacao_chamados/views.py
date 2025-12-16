from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator, has_role_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from rolepermissions.roles import assign_role
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'GET':
     return render(request, 'login_cadastro/login.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print(username, email, senha)
        user = User.objects.filter(username=username, email=email).first()
        if user:
            auth_login(request, user)
            user = authenticate(username=username, password=senha)
            return redirect('abrir_chamado')
        else:
            erro = 'Usuário não encontrado'
            return render(request, 'login_cadastro/login.html', {'erro': erro})

@has_role_decorator('administrator')
def cadastro(request):
    if request.method == 'GET':
     return render(request, 'login_cadastro/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        senha = request.POST.get('senha')
        print(username, email, role, senha)
        user = User.objects.filter(username=username, email=email).first()
        if user:
           erro = 'Usuário já cadastrado'
           return render(request, 'login_cadastro/cadastro.html', {'erro': erro})
        else:
            user = User.objects.create_user(username=username, email=email, password=senha)
            assign_role(user, role)
            return redirect('login')
   

def abrir_chamado(request):
    if request.method == 'GET':
     return render(request, 'abrir_chamado.html')
    else:
       nome = request.POST.get('nome')
       email = request.POST.get('email')
       relatar_problema = request.POST.get('relatar_problema')


@has_permission_decorator('visualizar_todos_chamados')
def visualizar_todos_chamados(request):
    return render(request, 'atendente/visualizar_todos_chamados.html')