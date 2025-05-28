from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Contacto, Login
from django.core.mail import send_mail, EmailMessage

# Create your views here.
def index(request, nombre = None):
    return render(request,"index/index.html", context= {"nombre": nombre})

def contactos(request):
    return render(request,"contactos/contacto.html")

def nosotros(request):
    return render(request,"nosotros/nosotros.html")

def login_page(request):
    return render(request,'sesion/sesion.html')

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            return redirect(reverse('index',kwargs={'nombre': form.cleaned_data["usuario"]}))
    print("form not valid")
    return redirect('index')
    
        
def contactar(request):
    if request.method == "POST":
        form = Contacto(request.POST)
        if form.is_valid():
            print(form)
            em = EmailMessage(
                "Consulta de " + form.cleaned_data["nombre"] + " " + form.cleaned_data["apellido"],
                "Esta es una consulta automatica de BoldWave.org\nDomicilio: "
                + form.cleaned_data["domicilio"] + "\nLocalidad: " + 
                form.cleaned_data["localidad"] + "\nTelefono: " +
                str(form.cleaned_data["telefono"]),
                form.cleaned_data["email"],
                ["consultas@boldwave.org"],
            )
            em.send()
            form.cleaned_data["nombre"]
        else:
            print("Form is not valid")
            print(form)
    return redirect('index')