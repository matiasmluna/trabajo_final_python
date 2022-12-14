"""practicaMVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from AppCoder.views import familiares, familiaresFormulario
from AppCoder.views import productos, productosFormulario
from AppCoder.views import profesiones, profesionesFormulario
from AppCoder.views import buscar, busquedaCamada, index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('familiares/', familiares, name="familiares"),
    path('productos/', productos, name="productos"),
    path('profesiones/', profesiones, name="profesiones"),
    path('familiaresFormulario/', familiaresFormulario, name="familiaresFormulario"),
    path('productosFormulario/', productosFormulario, name="productosFormulario"),
    path('profesionesFormulario/', profesionesFormulario, name="profesionesFormulario"),
    path('buscar/', buscar, name="buscar"),
    path('busquedaProductoPrecio', busquedaCamada, name="busquedaCamada"),
    path('accounts/login/', include('login.urls')),
    path('accounts/signup/', include('registro.urls')),
    path('accounts/perfil/', include('perfiles.urls')),
]
