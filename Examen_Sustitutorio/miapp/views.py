from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import Barrios_Usuarios
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def agregar_usuario(request):
    if request.method == 'POST':
        try:
            login = request.POST['Barrios_login']
            clave = request.POST['Barrios_clave']
            disponible = request.POST['Barrios_disponible']
            
            usuario = Barrios_Usuarios(
                Barrios_login=login,
                Barrios_clave=clave,
                Barrios_disponible=disponible
            )
            usuario.save()
            messages.success(request, 'El usuario ha sido agregado con éxito.')
            return redirect('usuarios')
        except KeyError as e:
            messages.error(request, f'Error en el formulario: {str(e)}')
    return render(request, 'agregar_usuario.html')

def editar_usuario(request, id):
    usuario = get_object_or_404(Barrios_Usuarios, id=id)
    if request.method == 'POST':
        usuario.Barrios_login = request.POST.get('Barrios_login', usuario.Barrios_login)
        usuario.Barrios_clave = request.POST.get('Barrios_clave', usuario.Barrios_clave)
        usuario.Barrios_disponible = request.POST.get('Barrios_disponible', usuario.Barrios_disponible)
        usuario.save()
        messages.success(request, 'El usuario ha sido actualizado con éxito.')
        return redirect('usuarios')
    return render(request, 'editar_usuario.html', {'usuario': usuario})


def usuarios(request):
    usuarios = Barrios_Usuarios.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Barrios_Usuarios, id=id)
    usuario.delete()
    messages.success(request, 'El usuario ha sido eliminado con éxito.')
    return redirect('usuarios')

