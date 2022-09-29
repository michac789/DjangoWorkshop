from django.urls import path
from . import views


app_name = "lesson"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_lesson, name="create"),
    path('<str:lesson_name>/', views.view_lesson, name="view"),
]
