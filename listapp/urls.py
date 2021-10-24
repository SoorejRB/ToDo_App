
from django.urls import path, include
from . import views

app_name = "listapp"
urlpatterns = [

    path('', views.IndexView.as_view(), name="indexpage"),
    path('add-task', views.AddTask.as_view(), name="addtaskpage"),
    path('add-tasktype', views.AddTaskType.as_view(), name="addtasktypepage"),

]