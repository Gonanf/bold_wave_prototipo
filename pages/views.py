from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index/index.html")

def contactos(request):
    return render(request,"contactos/contacto.html")

def nosotros(request):
    return render(request,"nosotros/nosotros.html")