from django.db import models
from django import forms
import datetime
from django.utils import timezone

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    seeds = models.IntegerField()
    peers = models.IntegerField()
    date = models.DateTimeField()
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['date']
    
class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    
    