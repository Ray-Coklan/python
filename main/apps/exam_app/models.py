from __future__ import unicode_literals
import datetime
from django.db import models
from ..first_app.models import *

class TravelManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Travel name cannot be empty"
        if len(postData['description']) < 1:
            errors['descriptioin'] = "Description cannot be empty"
        if datetime.datetime.strptime(postData['travel_date_from'], '%Y-%m-%d') < datetime.datetime.now():
            errors['date'] = "Date cannot be in the past, silly"
        if datetime.datetime.strptime(postData['travel_date_to'], '%Y-%m-%d') < datetime.datetime.now():
            errors['date'] = "Date cannot be in the past, silly"
        return errors

class Travel(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    objects = TravelManager()
    creator = models.ForeignKey(User, related_name="created_by")
    join = models.ManyToManyField(User, related_name="join_trip")
    
