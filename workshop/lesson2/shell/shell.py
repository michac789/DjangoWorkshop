"""
    This is to be executed via Django shell (for Topic 12),
    to demonstrate a simple CRUD operations for Django Models.
    
    You can find more detailed commands from Django's documentation:
    https://docs.djangoproject.com/en/4.1/ref/models/querysets/
"""

# import model
from lesson2.models import Lesson

# create
l1 = Lesson(title="math", content="some math content...")
l1.save()
l2 = Lesson(title="english", content="some english content...")
l2.save()
Lesson.objects.create(title="physics", content="some physics content...")

# read
Lesson.objects.all()
Lesson.objects.filter(title__in=["math", "english"])
Lesson.objects.order_by("-title")
Lesson.objects.all().count()
Lesson.objects.get(id=1)
x = Lesson.objects.get(id=2)
x.id
x.title
x.content

# update
x = Lesson.objects.get(id=1)
x.content = "edit math content..."
x.save()
Lesson.objects.get(id=1).content
Lesson.objects.filter(title="english").update(content="edit english content...")
Lesson.objects.get(title="english").content

# delete
x = Lesson.objects.get(id=2)
x.delete()
Lesson.objects.all()
Lesson.objects.filter(title="physics").delete()
Lesson.objects.all()
