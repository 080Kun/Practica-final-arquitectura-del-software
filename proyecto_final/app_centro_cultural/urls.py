from django.urls import path
from .views import lista_actividades, detalle_actividad,editar_actividad,eliminar_actividad,nueva_actividad
from .views import lista_usuarios, detalle_usuario,editar_usuario,eliminar_usuario,nuevo_usuario
from .views import lista_monitores, detalle_monitor,editar_monitor,eliminar_monitor,nuevo_monitor
from .views import lista_salas, detalle_sala,editar_sala,eliminar_sala,nueva_sala


urlpatterns = [
    path('actividades/', lista_actividades, name='lista_actividades'), 
    path('actividades/nueva/', nueva_actividad, name='nueva_actividad'),
    path('actividades/<id>/', detalle_actividad, name='detalle_actividad'),
    path('actividades/<id>/editar', editar_actividad, name='editar_actividad'),
    path('actividades/<id>/eliminar', eliminar_actividad, name='eliminar_actividad'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'), 
    path('usuarios/<id>/', detalle_usuario, name='detalle_usuario'),
    path('usuarios/nuevo/', nuevo_usuario, name='nuevo_usuario'),
    path('usuarios/<id>/editar', editar_usuario, name='editar_usuario'),
    path('usuarios/<id>/eliminar', eliminar_usuario, name='eliminar_usuario'),
    path('monitores/', lista_monitores, name='lista_monitores'),
    path('monitores/nuevo/', nuevo_monitor, name='nuevo_monitor'),
    path('monitores/<id>/', detalle_monitor, name='detalle_monitor'),
    path('monitores/<id>/editar', editar_monitor, name='editar_monitor'),
    path('monitores/<id>/eliminar', eliminar_monitor, name='eliminar_monitor'),
    path('salas/', lista_salas, name='lista_salas'),
    path('salas/nueva/', nueva_sala, name='nueva_sala'),
    path('salas/<id>/', detalle_sala, name='detalle_sala'),
    path('salas/<id>/editar', editar_sala, name='editar_sala'),
    path('salas/<id>/eliminar', eliminar_sala, name='eliminar_sala'),
]


