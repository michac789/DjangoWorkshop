from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    def __str__(self):
        return f"ID {self.id}: {self.title.capitalize()} Lesson"
