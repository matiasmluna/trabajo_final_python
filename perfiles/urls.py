from django.urls import path
from perfiles.views import editarPerfil
#from perfiles.views import 

urlpatterns = [
    path('', editarPerfil, name="editarPerfil"),
]
