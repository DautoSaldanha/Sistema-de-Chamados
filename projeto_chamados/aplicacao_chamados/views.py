from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator, has_permissions_decorator


def abrir_chamado(request):
    if request.method == 'GET':
     return render(request, 'abrir_chamado.html')
    else:
       pass


def visualizar_todos_chamados(request):
    return render(request, 'visualizar_todos_chamados.html')