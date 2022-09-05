from django.shortcuts import render, redirect
from registro.form import UserRegisterForm


def register(request):

      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return redirect('login')
                  #return render(request,"./practicaMVT/templates/inicio.html" ,  {"mensaje":"Usuario Creado"})
      else:    
            form = UserRegisterForm()     

      return render(request,"./practicaMVT/templates/registro/registro.html" ,  {"form":form})
      
