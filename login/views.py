from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(username=usuario, password=password)
                  if user is not None:
                        login(request, user)

                        return render(request,"./practicaMVT/templates/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
            
            form = AuthenticationForm()
            return render(request,"./practicaMVT/templates/login/login.html", {'error':'Formulario inválido','form':form} )
      elif request.method == "GET":
            form = AuthenticationForm()
            return render(request,"./practicaMVT/templates/login/login.html", {'form':form} )
      

