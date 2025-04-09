from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('crear/', views.habit_create, name='create_habit'),
    path('editar/<int:pk>/', views.habit_edit, name='edit_habit'), 
    path('eliminar/<int:pk>/', views.habit_delete, name='delete_habit'),
]
