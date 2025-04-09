from django import forms
from .models import Habit

class Habit(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description']
