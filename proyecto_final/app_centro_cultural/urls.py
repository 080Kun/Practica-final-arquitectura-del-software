from django.urls import path
from .views import lista_actividades, detalle_actividad,editar_actividad,eliminar_actividad,nueva_actividad
#from .views import lista_usuarios, detalle_usuarios,editar_usuarios,eliminar_usuarios,nueva_usuarios



urlpatterns = [
    path('actividades/', lista_actividades, name='lista_actividades'), 
    path('actividades/nueva/', nueva_actividad, name='nueva_actividad'),
    path('actividades/<id>/', detalle_actividad, name='detalle_actividad'),
    path('actividades/<id>/editar', editar_actividad, name='editar_actividad'),
    path('actividades/<id>/eliminar', eliminar_actividad, name='eliminar_actividad'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'), 
    path('usuarios/<id>/', detalle_usuarios, name='detalle_usuarios'),
    path('usuarios/nueva/', nueva_usuarios, name='nueva_usuarios'),
    path('usuarios/<id>/editar', editar_usuarios, name='editar_usuarios'),
    path('usuarios/<id>/eliminar', eliminar_usuarios, name='eliminar_usuarios'),
]


