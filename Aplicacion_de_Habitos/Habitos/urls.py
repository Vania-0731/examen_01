from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('crear/', views.habit_create, name='habit_create'),  # Cambié de 'create_habit' a 'habit_create'
]
