from django.shortcuts import render, redirect
from .models import Habit
from .forms import HabitForm

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habitos/habit_list.html', {'habits': habits})

def habit_create(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habits/habit_form.html', {'form': form})

# Create your views here.
