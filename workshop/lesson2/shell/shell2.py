"""
    This is to be executed via Django shell (for Topic 15),
    to demonstrate relationships in a foreign key (one to many).
"""

# import model
from lesson2.models import Lesson, Student

# getting lesson from the student object
x = Student.objects.get(id=1)
x.course
x.course.content

# getting students from the lesson object
y = Lesson.objects.get(id=1)
y.students.all()
