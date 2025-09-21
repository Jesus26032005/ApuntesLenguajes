from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse("¡Bienvenido a mi sitio web!")

def despedida(request):
    return HttpResponse("¡Hasta luego!")
