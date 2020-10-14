from django import forms

from .models import *

class taskForm(forms.ModelForm):

    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = task
        fields = '__all__'