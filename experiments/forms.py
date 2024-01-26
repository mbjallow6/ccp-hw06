# forms.py
from django import forms
import datetime
# from .models import Experiment


class ExperimentForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    title = forms.CharField(max_length=200, initial='Untitled Experiment')
    short_description = forms.CharField(max_length=500, initial='No description provided.', widget=forms.Textarea)
    detail_description = forms.CharField(widget=forms.Textarea, initial='Detailed description not available.')
    owner_name = forms.CharField(max_length=100, initial='Anonymous')
    STATUS_CHOICES = [('completed', 'Completed'), ('ongoing', 'Ongoing')]
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial='ongoing')



# the code below was used for homework 6

# class ExperimentForm(forms.ModelForm):
#     class Meta:
#         model = Experiment
#         fields = ['date', 'title', 'short_description', 'detail_description', 'owner_name', 'status']


