from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('crear/', views.create_habit, name='create_habit'),
]
