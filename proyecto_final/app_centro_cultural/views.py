from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Actividad, Inscripcion, Usuario, Monitor, Sala
from django.shortcuts import render, redirect
from .forms import ActividadForm, UsuarioForm


#Actividad
def lista_actividades(request):
    actividades = Actividad.objects.all() 
    return render(request, 'app_centro_cultural/lista_actividades.html', {'actividades': actividades})

def detalle_actividad(request, actividad_id):
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        monitor = Monitor.objects.get(monitor=monitor)
        contexto = {
            'actividad': actividad,
            'monitor': monitor,
        }
        return render(request, 'app_centro_cultural/detalle_Actividad.html', contexto)
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrado"}, status=404)
    
@csrf_exempt
def nueva_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'app_centro_cultural/formulario.html', {'form': form, 'titulo': 'Nueva Actividad'})


@csrf_exempt
def editar_actividad(request, actividad_id):
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        
        if request.method == 'PUT':
            form = ActividadForm(request.PUT,instance=actividad)
            if form.is_valid():
                form.save()
                return redirect('lista_actividades')
        else:
            form = ActividadForm()
        return render(request, 'app_centro_cultural/formulario_put.html', {'form': form, 'titulo': 'Actualizar Actividad'})

    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrado"}, status=404)

@csrf_exempt
def eliminar_actividad(request, actividad_id):
    
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        
        if request.method == 'DELETE':
            actividad.delete()
            return redirect('lista_actividades')
    except Actividad.DoesNotExist:
        return JsonResponse({"error": "Actividad no encontrado"}, status=404)


#Usuario
def lista_usuarios(request):
    usuarios = Usuario.objects.all() 
    return render(request, 'app_centro_cultural/lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        return render(request, 'app_centro_cultural/detalle_Actividad.html', usuario)
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    
@csrf_exempt
def nuevo_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'app_centro_cultural/formulario.html', {'form': form, 'titulo': 'Nuevo Usuario'})


@csrf_exempt
def editar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
        if request.method == 'PUT':
            form = UsuarioForm(request.PUT,instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('lista_usuarios')
        else:
            form = UsuarioForm()
        return render(request, 'app_centro_cultural/formulario_put.html', {'form': form, 'titulo': 'Actualizar Usuario'})

    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)

    


@csrf_exempt
def eliminar_usuario(request, usuario_id):
    
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
        if request.method == 'DELETE':
            usuario.delete()
            return redirect('lista_usuarios')
    except Usuario.DoesNotExist:
        return JsonResponse({"error": "Usuario no encontrado"}, status=404)