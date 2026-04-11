from . import views
from django.urls import path

urlpatterns=[
    path("", views.task_list, name="index"),
    path("addTask/", views.add_task, name="addTask")
]