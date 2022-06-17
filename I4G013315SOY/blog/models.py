from operator import mod
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Post (models.Model):
    Title = models.CharField(max_length=200, blank=False)
    Text = models.TextField(blank=False)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(blank=False)
    Published_Date = models.DateTimeField(blank=False)
    
    def __str__(self):
        return self.title