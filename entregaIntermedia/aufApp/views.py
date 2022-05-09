from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def equipos(request):
    if request.method == 'POST':
        formulario = EquipoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            equipo = Equipos(nombre=informacion['nombre'],direccionSede=informacion['direccionSede'],email=informacion['email'],fechaFundacion=informacion['fechaFundacion'])
            equipo.save()
            return render(request,'home.html')
    else:
        formulario = EquipoFormulario()
        return render(request,'equipos.html',{'formulario':formulario})
    

def estadios(request):
    if request.method == 'POST':
        formulario = EstadioFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estadio = Estadio(nombre=informacion['nombre'],direccion=informacion['direccion'],fechaConstruccion=informacion['fechaConstruccion'],propietario=informacion['propietario'])
            estadio.save()
            return render(request,'home.html')
    else:
        formulario = EstadioFormulario()
        return render(request,'estadios.html',{'formulario':formulario})

def futbolistas(request):
    if request.method == 'POST':
        formulario = FutbolistaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            futbolista = Futbolista(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],fechaNacimiento=informacion['fechaNacimiento'])
            futbolista.save()
            return render(request,'home.html')
    else:
        formulario = FutbolistaFormulario()
        return render(request,'futbolistas.html',{'formulario':formulario})