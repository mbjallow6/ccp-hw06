from django.shortcuts import render
from .models import Experiment

def index(request):
    experiments = Experiment.objects.all()
    return render(request, 'experiments/index.html', {'experiments': experiments})

def detail(request, experiment_id):
    experiment = Experiment.objects.get(pk=experiment_id)
    return render(request, 'experiments/detail.html', {'experiment': experiment})

def submit_experiment(request):
    # Your code to handle the form submission
    return render(request, 'experiments/submit_experiment.html')
