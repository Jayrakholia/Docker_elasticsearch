from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
#user model
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField() 
    gender = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#competition model
class Competition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#entry model
class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    competition_id = models.ForeignKey(Competition, on_delete=models.CASCADE)
