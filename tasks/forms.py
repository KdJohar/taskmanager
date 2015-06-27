from django import forms
from models import Task
class TaskCreationForm(forms.ModelForm):
    name = forms.CharField(label='Task Name')
    date = forms.DateField(label='Deadline Date')
    description = forms.Textarea()

    class Meta:
        model = Task
        fields = ['name', 'date', 'description']


