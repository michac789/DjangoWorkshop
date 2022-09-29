from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    def __str__(self):
        return f"ID {self.id}: {self.title.capitalize()} Lesson"


class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
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
    
    def __str__(self):
        return f"Student ID {self.id}: {self.name}"
