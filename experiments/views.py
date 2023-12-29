from django.shortcuts import render, redirect
from .models import Experiment
from .forms import ExperimentForm

def home(request):
    experiments = Experiment.objects.all()  
    return render(request, 'experiments/home.html', {'experiments': experiments})


def about(request):
    # Redirect to my pfofile page
    return redirect('https://mbjallow.com')

def submit_new_entry(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiments:home')
    else:
        form = ExperimentForm()
    return render(request, 'experiments/submit_new_entry.html', {'form': form})

def detail(request, experiment_id):
    # Detail view of an experiment
    experiment = Experiment.objects.get(pk=experiment_id)
    return render(request, 'experiments/detail.html', {'experiment': experiment})






