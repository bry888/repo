from django.db import models
from django import forms
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

class AddEventForm(forms.Form):
    title = forms.CharField(max_length=200)
    date_time = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'text', 'rows':'8'}))
    location = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)