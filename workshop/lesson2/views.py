from django.shortcuts import render
from .models import Lesson, Student


def index(request):
    return render(request, "lesson2/index.html", {
        "lessons": Lesson.objects.all(),
        "students": Student.objects.all()
    })
