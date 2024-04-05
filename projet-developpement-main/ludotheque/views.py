from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenue(request):
    return HttpResponse('<h1>Bienvenue  à notre ludotheque!</h1>')

def accueil(request):
    pass
def connecxion(request):
    pass

def inscription(request):
    pass
def liste_des_jeux(request):
    pass

def jeux_emprunte(request):
    pass

def parametres(request):
    pass

def creation_jeux(request):
    pass
def modification_jeux(request):
    pass

def liste_utilisayeur(request):
    pass

def creation_utilisayeur(request):
    pass

def modification_utilisayeur(request):
    pass