from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1> Mi primera vista Django</h1>")
