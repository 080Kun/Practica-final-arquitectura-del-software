from django import forms
from .models import Actividad, Usuario

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

