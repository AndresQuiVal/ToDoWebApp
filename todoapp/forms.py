from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["name", "description", "date", "priority"]
        widgets = {
             "description" : forms.Textarea(attrs={'placeholder': 'Enter the description'}),
             "name" : forms.TextInput(attrs={'placeholder' : 'Enter your todo name'}),
        }
