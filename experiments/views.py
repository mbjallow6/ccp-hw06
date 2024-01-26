from django.shortcuts import render, redirect
from mongo_db_connection import get_collection
from bson.objectid import ObjectId
from .forms import ExperimentForm, SearchForm
import datetime

def home(request):
    collection = get_collection()
    experiments = list(collection.find({}))

    for experiment in experiments:
        experiment['str_id'] = str(experiment['_id'])
    return render(request, 'experiments/home.html', {'experiments': experiments})


def about(request):
    # Redirect to my profile page
    return redirect('https://mbjallow.com')

def submit_new_entry(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            collection = get_collection()
            experiment_data = form.cleaned_data
            experiment_data['date'] = experiment_data['date'].strftime('%Y-%m-%d')  # Format date to string
            collection.insert_one(experiment_data)
            return redirect('experiments:home')
    else:
        form = ExperimentForm()
    return render(request, 'experiments/submit_new_entry.html', {'form': form})

def detail(request, experiment_id):
    collection = get_collection()
    experiment = collection.find_one({'_id': ObjectId(experiment_id)})
    experiment['str_id'] = str(experiment['_id'])
    return render(request, 'experiments/detail.html', {'experiment': experiment})

def search(request):
    form = SearchForm(request.GET or None)
    experiments = []

    if form.is_valid():
        query = {}
        # Add title filter
        if form.cleaned_data['title']:
            query['title'] = {'$regex': form.cleaned_data['title'], '$options': 'i'}
        # Add owner name filter
        if form.cleaned_data['owner_name']:
            query['owner_name'] = {'$regex': form.cleaned_data['owner_name'], '$options': 'i'}
        # Add date filter
        if form.cleaned_data['date']:
            query['date'] = str(form.cleaned_data['date'])
        # Add status filter
        if form.cleaned_data['status']:
            query['status'] = form.cleaned_data['status']

        collection = get_collection()
        experiments = list(collection.find(query))

        for experiment in experiments:
            experiment['str_id'] = str(experiment['_id'])

    return render(request, 'experiments/search.html', {'form': form, 'experiments': experiments})


# from .models import Experiment

# the code belw was used for homework 6 
    # experiments = Experiment.objects.all()  
    # return render(request, 'experiments/home.html', {'experiments': experiments})


# def about(request):
#     # Redirect to my pfofile page
#     return redirect('https://mbjallow.com')

# def submit_new_entry(request):
#     if request.method == 'POST':
#         form = ExperimentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('experiments:home')
#     else:
#         form = ExperimentForm()
#     return render(request, 'experiments/submit_new_entry.html', {'form': form})

# def detail(request, experiment_id):
#     # Detail view of an experiment
#     experiment = Experiment.objects.get(pk=experiment_id)
#     return render(request, 'experiments/detail.html', {'experiment': experiment})






