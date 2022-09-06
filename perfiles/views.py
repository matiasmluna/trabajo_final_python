from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from perfiles.form import UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@login_required
def editarPerfil(request):
      
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 

            if miFormulario.is_valid:  
                  informacion = miFormulario
                  #informacion = miFormulario.cleaned_data.get()
                  
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.imagen_avatar = informacion['imagen_avatar']

                  usuario.save()
                  return render(request, "./practicaMVT/templates/inicio.html", {"mensaje":f"Los cambios de {usuario} fueron realizados"}) #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 
            return render(request, "./practicaMVT/templates/perfil/editprofile.html", {"miFormulario":miFormulario, "usuario":usuario})