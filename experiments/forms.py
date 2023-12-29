# forms.py
from django import forms
from .models import Experiment

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['date', 'title', 'short_description', 'detail_description', 'owner_name', 'status']


