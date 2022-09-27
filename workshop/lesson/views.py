from django.shortcuts import render


valid_lessons = [
    "math", "english", "physics"
]


def index(request):
    return render(request, "lesson/index.html")


def view_lesson(request, lesson_name):
    return render(request, "lesson/view_lesson.html", {
        "title": lesson_name.capitalize(),
        "valid": lesson_name in valid_lessons,
    })
