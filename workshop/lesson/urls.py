from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<str:lesson_name>/', views.view_lesson),
]
