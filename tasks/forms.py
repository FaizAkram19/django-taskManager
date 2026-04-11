from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields = ["priorityLevel", "title", "description", "due_date"]
        widgets = { 
            'due_date': forms.TextInput(attrs={'autocomplete': 'off'})
            #had to add this widget part because Django was rendering due_date as type="datetime-local", which conflicts with Flatpickr.
            #(the CSS module to show a calender and clock for picking datetime) This gives Flatpickr full control over the field
            #  — no native browser picker interfering
        }
        #Django's DateTimeField automatically renders as <input type="datetime-local"> in HTML. 
        # That input type has its own built-in browser date picker baked in.
        #Flatpickr works by attaching itself to a text input and building its own calendar UI. 
        # When you put Flatpickr on a datetime-local input, two pickers are fighting over the same field
        #  — the browser's native one and Flatpickr's. That's why clicking outside doesn't close it properly.
        #Changing the widget to TextInput makes Django render it as <input type="text"> instead
        #  — a plain field with no built-in behavior — so Flatpickr has full control.
