from django.urls import path
from perfiles.views import editarPerfil

urlpatterns = [
    path('', editarPerfil, name="editarPerfil"),
]
