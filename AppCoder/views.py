from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

def curso(self):
    curso=Curso(nombre="Django", comision=939393)
    curso.save()
    texto= f"curso creado: {curso.nombre}{curso.comision}"
    return HttpResponse(texto)
# Create your views here.
