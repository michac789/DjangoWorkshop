from django.shortcuts import render


def index(request):
    return render(request, "lesson2/index.html")