"""
URL configuration for bold_wave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<str:nombre>', views.index,name='index'),
    path('nosotros/', views.nosotros,name='nosotros'),
    path('contactos/', views.contactos,name='contactos'),
    path('login_page/',views.login_page,name='login_page'),
    path('login_page/login/',views.login,name='login'),
    path('contactos/contactar/',views.contactar,name="contactar"),
]
