from django.template import loader
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context
from AppCoder.form import FamiliarFormulario, ProfesionesFormulario, ProductosFormulario


# Create your views here.
from django.http import HttpResponse
from AppCoder.models import Familiares, Profesiones, Articulos

def familiares(resquest):
    
    familiar = Familiares.objects.all()
    context = {
        "familiar":familiar
    }

    return render(resquest, './practicaMVT/templates/familiares.html', context=context)

def profesiones(resquest):
    
    profesion = Profesiones.objects.all()
    context = {
        'profesion':profesion
    }

    return render(resquest, './practicaMVT/templates/profesiones.html', context=context)

def productos(resquest):
    
    articulo = Articulos.objects.all()
    context = {
        "articulo":articulo
    }

    return render(resquest, './practicaMVT/templates/productos.html', context=context)


def familiaresFormulario(request):

    if request.method == 'POST':
        
        miFormulario = FamiliarFormulario(request.POST) #aquí mellega toda la información del html
        
        print(miFormulario)
        
        if miFormulario.is_valid:   #Si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data

            familiar = Familiares(
                nombre=informacion['nombre'], 
                fechaDeNacimiento=informacion['fechaDeNacimiento'],
                edad=informacion['edad'], 
                ) 

            familiar.save()

            return render(request, './practicaMVT/templates/familiares.html') #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= FamiliarFormulario() #Formulario vacio para construir el html

    return render(request,'./practicaMVT/templates/familiaresFormulario.html', {'miFormulario':miFormulario})


def productosFormulario(request):

    if request.method == 'POST':
        
        miFormulario = ProductosFormulario(request.POST) #aquí mellega toda la información del html
        
        print(miFormulario)
        
        if miFormulario.is_valid:   #Si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data

            articulo = Articulos(
                nombre_articulo=informacion['nombre_articulo'], 
                stock=informacion['stock'],
                precio=informacion['precio'], 
                ) 

            articulo.save()

            return render(request, './practicaMVT/templates/productos.html') #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= ProductosFormulario() #Formulario vacio para construir el html

    return render(request,'./practicaMVT/templates/productosFormulario.html', {'miFormulario':miFormulario})


def profesionesFormulario(request):

    if request.method == 'POST':
        
        miFormulario = ProfesionesFormulario(request.POST) #aquí mellega toda la información del html
        
        print(miFormulario)
        
        if miFormulario.is_valid:   #Si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data

            profesion = Profesiones(
                profesion=informacion['profesion'], 
                sueldo=informacion['sueldo'],
                ) 

            profesion.save()

            return render(request, './practicaMVT/templates/profesiones.html') #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= ProfesionesFormulario() #Formulario vacio para construir el html

    return render(request,'./practicaMVT/templates/profesionesFormulario.html', {'miFormulario':miFormulario})


def busquedaCamada(resquest):

    return render(resquest, './practicaMVT/templates/buscador.html')

def index(resquest):

    return render(resquest, './practicaMVT/templates/index.html')


def buscar(request):

    if  request.GET['precio']:
        precio = request.GET['precio'] 
        articulos = Articulos.objects.filter(precio__icontains=precio)
        return render(request, './practicaMVT/templates/buscador.html', {'articulos':articulos, 'precio':precio})
    else: 
	    respuesta = 'Por favor carga un dato'
#    respuesta = f"Estoy buscando el precio nro: {request.GET['precio'] }" 
    return HttpResponse(respuesta)