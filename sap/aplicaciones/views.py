import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona
# Create your views here.

def bienvenido(request):
    nro_personas_var=Persona.objects.count
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id', 'nombre')

    return render(request, 'bienvenido.html', {'nro_personas':nro_personas_var, 'personas': personas})