from . import views
from django.urls import path

urlpatterns=[
    path("", views.task_list, name="index"),
    path("addTask/", views.add_task, name="addTask"),
    path("<int:pk>/edit/", views.edit_task, name="edit"),
    path("<int:pk>/deleteTask/", views.delete_task, name="deleteTask")
]