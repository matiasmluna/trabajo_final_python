from django import forms

class FamiliarFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    fechaDeNacimiento = forms.DateField()
    edad = forms.IntegerField()

class ProfesionesFormulario(forms.Form):
    profesion= forms.CharField(max_length=30)
    sueldo = forms.IntegerField()

class ProductosFormulario(forms.Form):
    nombre_articulo= forms.CharField(max_length=30)
    stock = forms.IntegerField()
    precio = forms.IntegerField()