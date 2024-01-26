from django.db import models
# from mongo_db_connection import db
import datetime

class Experiment(models.Model):
    date = models.DateField(default=datetime.date.today)  # Default to today's date
    title = models.CharField(max_length=200, default='Untitled Experiment')  # Default title
    short_description = models.CharField(max_length=300, default='No description provided.')  # Default short description
    detail_description = models.TextField(default='Detailed description not available.')  # Default detailed description
    owner_name = models.CharField(max_length=100, default='Anonymous')  # Default owner name
    STATUS_CHOICES = [('completed', 'Completed'), ('ongoing', 'Ongoing')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')  # Default status


    

    def __str__(self):
        return self.title
