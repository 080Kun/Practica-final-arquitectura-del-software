from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Actividad, Inscripcion, Usuario, Monitor, Sala
from django.shortcuts import render, redirect
from .forms import ActividadForm, UsuarioForm, MonitorForm, SalaForm


#Actividad
def lista_actividades(request):
    actividades = Actividad.objects.all() 
    return render(request, 'app_centro_cultural/actividades/lista_actividades.html', {'actividades': actividades})

def detalle_actividad(request, actividad_id):
    try:
        actividad = Actividad.objects.get(id=actividad_id)
        monitor = Monitor.objects.get(id=actividad.monitor_id)
        sala = Sala.objects.get(id=actividad.sala_id)
        contexto = {
            'actividad': actividad,
            'monitor': monitor,
            'sala': sala
        }
        return render(request, 'app_centro_cultural/actividades/detalle_actividad.html', contexto)
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
    return render(request, 'app_centro_cultural/usuarios/lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        return render(request, 'app_centro_cultural/usuarios/detalle_usuario.html', {'usuario': usuario})
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
    
# MONITOR

def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'app_centro_cultural/monitores/lista_monitores.html', {'monitores': monitores})


def detalle_monitor(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        return render(request, 'app_centro_cultural/monitores/detalle_monitor.html', {'monitor': monitor})
    
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)


@csrf_exempt
def nuevo_monitor(request):

    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_monitores')
    else:
        form = MonitorForm()

    return render(request, 'app_centro_cultural/formulario.html', {
        'form': form,
        'titulo': 'Nuevo Monitor'
    })


@csrf_exempt
def editar_monitor(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        if request.method == 'POST':
            form = MonitorForm(request.POST, instance=monitor)
            if form.is_valid():
                form.save()
                return redirect('lista_monitores')
        else:
            form = MonitorForm(instance=monitor)

        return render(request, 'app_centro_cultural/formulario_put.html', {
            'form': form,
            'titulo': 'Actualizar Monitor'
        })

    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)


@csrf_exempt
def eliminar_monitor(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        if request.method == 'POST':
            monitor.delete()
            return redirect('lista_monitores')
    except Monitor.DoesNotExist:
        return JsonResponse({"error": "Monitor no encontrado"}, status=404)


# SALA

def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'app_centro_cultural/salas/lista_salas.html', {'salas': salas})


def detalle_sala(request, sala_id):

    try:
        sala = Sala.objects.get(id=sala_id)
        return render(request, 'app_centro_cultural/salas/detalle_sala.html', {'sala': sala})

    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)


@csrf_exempt
def nueva_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm()

    return render(request, 'app_centro_cultural/formulario.html', {
        'form': form,
        'titulo': 'Nueva Sala'
    })


@csrf_exempt
def editar_sala(request, sala_id):
    try:
        sala = Sala.objects.get(id=sala_id)
        if request.method == 'POST':
            form = SalaForm(request.POST, instance=sala)

            if form.is_valid():
                form.save()
                return redirect('lista_salas')
        else:
            form = SalaForm(instance=sala)
        return render(request, 'app_centro_cultural/formulario_put.html', {
            'form': form,
            'titulo': 'Actualizar Sala'
        })
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)


@csrf_exempt
def eliminar_sala(request, sala_id):
    try:
        sala = Sala.objects.get(id=sala_id)
        if request.method == 'POST':
            sala.delete()
            return redirect('lista_salas')
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)