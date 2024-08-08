from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks')
]
