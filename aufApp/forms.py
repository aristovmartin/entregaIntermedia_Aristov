from django import forms

class EquiposFormularios(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccionSede = forms.CharField(max_length=50)
    email = forms.EmailField()
    fechaCreacion = forms.DateTimeField()
    
class JugadoresFormularios(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    fechaNacimiento = forms.EmailField()
    
class EstadiosFormularios(forms.Form):
    direccion = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    fechaInauguracion = forms.EmailField()
    propietario = forms.CharField(max_length=50)