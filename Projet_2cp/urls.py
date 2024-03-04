"""
URL configuration for Projet_2cp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from lmcs.views import create_chercheur 
from lmcs.views import create_etudiant
from lmcs.views import home_page
from lmcs.views import search_chercheur

urlpatterns = [
    path('create_chercheur/', create_chercheur, name='create_chercheur'),
    path('', home_page, name='home'),
    path('Add_etudiant/', create_etudiant, name='create_etudiant'),
    path('Affich_chercheur/', search_chercheur, name='search_chercheur'),
]
