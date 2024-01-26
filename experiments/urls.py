from django.urls import path
from . import views

app_name = 'experiments'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('submit/', views.submit_new_entry, name='submit_new_entry'),
    path('detail/<str:experiment_id>/', views.detail, name='detail'),
    
]
