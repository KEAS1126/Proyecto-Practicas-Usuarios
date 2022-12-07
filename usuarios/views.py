from django.shortcuts import render, redirect
from usuarios.forms import *
from usuarios.models import Usuarios

# Create your views here.

def crearUsuario(request):
    if request.method == 'POST':
        formulario_usuario = FormularioUsuarios(request.POST, request.FILES)
        if formulario_usuario.is_valid():
            formulario_usuario.save()
            return redirect('/listar/')
    else:
        formulario_usuario = FormularioUsuarios()
    contexto = {'formulario_usuario': formulario_usuario}
    return render(request, 'crearUsuario.html', contexto)

def listarUsuarios(request):
    usuario=Usuarios.objects.filter()
    contexto={'usuario':usuario}
    return render(request, 'listarUsuarios.html',contexto)

