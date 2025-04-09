from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'habitos/habit_form.html', {'form': form})

def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit_list')  


def habit_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_list')  
    else:
        form = HabitForm(instance=habit)

    return render(request, 'habitos/habit_form.html', {'form': form})