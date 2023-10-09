import datetime
from django.http import HttpResponse

def principal(request):

    return HttpResponse("principal")

def carreras(request):

    return HttpResponse("carreras")

def pensum(request):

    return HttpResponse("esta es la pagina de pensum")

from django.shortcuts import render

def usuario(request):
    return render(request, 'usuario.html')
