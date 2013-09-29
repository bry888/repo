from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

    #class Meta:
        #unique_together = ['username', 'email']

''' for each model: form for validation etc
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
'''

class Articles(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    url = models.URLField()
    read_freq = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title, self.read_freq

    class Meta:
        ordering = ['read_freq']

class ArticlesReadByUser(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Articles)
    read_time = models.IntegerField(default=0)
    #opinion = models.NullBooleanField(default=null)
    def __unicode__(self):
        return self.title, self.read_time

    class Meta:
        ordering = ['user'] # ['title'] ?
    
class ArticlesToShow(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Articles)
    def __unicode__(self):
        return self.title
    
    class Meta:
        #? indexing = ['user']

'''
class User(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name="uzytkownik") #tylko 1 konto
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
'''
