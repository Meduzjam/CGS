from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ёмаё это мое первое приложене на Django ")

# Create your views here.
