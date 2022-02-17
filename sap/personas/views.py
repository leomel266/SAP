from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from personas.form import PersonaForm
from personas.models import Persona

# Create your views here.

def detallePersona(request,id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas\detalle.html', {'persona': persona})

#PersonaForm = modelform_factory(Persona, exclude=[])

def editarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)

    if request.method == 'POST':
        formaPersona= PersonaForm(request.POST, instance= persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')


    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})    

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona= PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index') 

    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})    


def eliminarPersona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

    

