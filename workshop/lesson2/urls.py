from django.urls import path
from . import views


app_name = "lesson2"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_student, name="create_student"),
]
