from django.contrib import admin
from .models import Lesson, Student


class LessonAdmin(admin.ModelAdmin):
    fields = ("title", "content")
    list_display = ("id", "title")
    ordering = ("title",)
    

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student)
