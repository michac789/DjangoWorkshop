from django.shortcuts import render


def index(request):
    return render(request, "lesson/index.html")


def view_lesson(request, lesson_name):
    # print(lesson_name)
    return render(request, "lesson/view_lesson.html", {
        "title": lesson_name.capitalize(),
    })
