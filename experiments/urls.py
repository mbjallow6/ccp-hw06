from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:experiment_id>/', views.detail, name='detail'),
    path('submit/', views.submit_experiment, name='submit_experiment'),

]
