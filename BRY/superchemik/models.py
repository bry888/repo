from django.db import models
from django import forms
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse


class Page(models.Model):
    image_name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('mainpage', kwargs={'page_id': self.id})
    
    #def get_absolute_url_next(self):
    #    if self.id == max(self.id):
    #        return reverse('superchemik.views.mainpage', args=(max(self.id)-1,))
    #    return reverse('superchemik.views.mainpage', args=(self.id+1,))
    #def get_absolute_url_prev(self):
    #    if self.id == 1:
    #        return reverse('superchemik.views.mainpage', args=(self.id,))
    #    return reverse('superchemik.views.mainpage', args=(self.id-1,))


class Comment(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateTimeField()
    content = models.TextField()
    page_num = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['date']
    
    
class CommentForm(forms.Form):
    name = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'text', 'rows':'8'}))
    #content = forms.CharField(widget=forms.TextInput(attrs={'class':'text', 'rows':'8'}))