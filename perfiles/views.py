from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from perfiles.form import UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@login_required
def editarPerfil(request):
      #Instancia del login
      usuario = request.user
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()
                  return render(request, "./practicaMVT/templates/perfil/editprofile.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 
            return render(request, "./practicaMVT/templates/perfil/editprofile.html", {"miFormulario":miFormulario, "usuario":usuario})