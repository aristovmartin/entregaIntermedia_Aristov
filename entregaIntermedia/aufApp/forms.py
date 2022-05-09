from django import forms

class EquipoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccionSede = forms.CharField(max_length=50)
    email = forms.EmailField()
    fechaFundacion = forms.DateField()
    
class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    fechaNacimiento = forms.DateField()
    
class EstadioFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    fechaConstruccion = forms.DateField()
    propietario = forms.CharField(max_length=50)