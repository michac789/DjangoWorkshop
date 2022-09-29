from django.shortcuts import render, redirect


valid_lessons = [
    "math", "english", "physics", "chemistry", "biology",
]


def index(request):
    # handle query parameter (if ?sort=true -> sort the lessons before displaying)
    lessons = valid_lessons
    if 'sort' in request.GET and request.GET["sort"] == "true":
        lessons = sorted(valid_lessons)
    
    return render(request, "lesson/index.html", {
        "lessons": lessons,
    })


def view_lesson(request, lesson_name):
    return render(request, "lesson/view_lesson.html", {
        "title": lesson_name.capitalize(),
        "valid": lesson_name in valid_lessons,
    })


def create_lesson(request):
    if request.method == "POST":
        new_lesson = request.POST["lesson_name"]

        # simple manual error checking, rerender form and show error message if any
        error = None
        if len(new_lesson.strip().lower()) == 0:
            error = "Lesson name cannot be empty!"
        if new_lesson.strip().lower() in valid_lessons:
            error = "No duplicate lessons are allowed!"
        if error:
            return render(request, "lesson/create.html", {
                "error": error,
            })
        
        valid_lessons.append(new_lesson.strip().lower())
        return redirect("lesson:index")
    else:
        return render(request, "lesson/create.html")
