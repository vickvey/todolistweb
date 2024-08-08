from django import forms
from main import models

class CreateTask(forms.ModelForm):
    class Meta:
        model=models.Task
        fields=['name', 'description']

class UpdateTask(forms.ModelForm):
    class Meta:
        model=models.Task
        fields=['done']