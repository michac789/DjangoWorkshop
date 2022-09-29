from django.shortcuts import render, redirect


valid_lessons = [
    "math", "english", "physics"
]


def index(request):
    return render(request, "lesson/index.html", {
        "lessons": valid_lessons,
    })


def view_lesson(request, lesson_name):
    return render(request, "lesson/view_lesson.html", {
        "title": lesson_name.capitalize(),
        "valid": lesson_name in valid_lessons,
    })


def create_lesson(request):
    if request.method == "POST":
        new_lesson = request.POST["lesson_name"]
        valid_lessons.append(new_lesson)
        return redirect("lesson:index")
    else:
        return render(request, "lesson/create.html")
