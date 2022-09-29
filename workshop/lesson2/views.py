from django.shortcuts import render, redirect
from .models import Lesson, Student
from .forms import StudentForm


def index(request):
    return render(request, "lesson2/index.html", {
        "lessons": Lesson.objects.all(),
        "students": Student.objects.all()
    })
    
    
def create_student(request):
    form = None
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return redirect("lesson2:index")
    return render(request, "lesson2/create_student.html", {
        "form": form or StudentForm(),
    })
