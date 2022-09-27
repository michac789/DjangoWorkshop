from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("<h1>hello world</h1>")


def homepage(request):
    return render(request, "myfirstapp/index.html")
