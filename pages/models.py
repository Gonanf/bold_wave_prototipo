from django.db import models
from django import forms

class Contacto(forms.Form):
    nombre = forms.CharField(label="nombre", max_length=30)
    apellido = forms.CharField(label="apellido", max_length=30)
    domicilio = forms.CharField(label="domicilio", max_length=100)
    localidad = forms.CharField(label="localidad", max_length=100)
    telefono = forms.CharField(label="telefono",widget=forms.NumberInput)
    email = forms.EmailField(label="email")

class Login(forms.Form):
    usuario = forms.CharField(label="usuario", max_length=100)
    contraseña = forms.CharField(label="contraseña", max_length=100)