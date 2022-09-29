from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator


class Lesson(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(validators=[MaxLengthValidator(1000)])
    
    def __str__(self):
        return f"ID {self.id}: {self.title.capitalize()} Lesson"


class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(100)
    ])
    course = models.ForeignKey(
        Lesson,
        # one student can only take 1 lesson, 
        # but 1 lesson can have many different students
        on_delete=models.CASCADE,
        # this option means: if the lesson is deleted, the student
        # that has it as a foreign key will also be deleted
        related_name="students"
        # you can access the students correlated through the lessons object
        # the reverse accessor: <LessonObject>.<related_name>.all()
    )
    register_time = models.DateTimeField(auto_now=True)
    
    EDUCATION_OPTIONS = [
        ("PR", "Primary"),
        ("SE", "Secondary"),
        ("JC", "Junior College"),
        ("UN", "University")
    ]
    education = models.CharField(choices=EDUCATION_OPTIONS, max_length=2, null=True)
    
    def __str__(self):
        return f"Student ID {self.id}: {self.name}"
