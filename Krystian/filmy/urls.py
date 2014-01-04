from django.conf.urls import patterns, url

from filmy import views

urlpatterns = patterns('',
    url(r'^$', views.filmy, name='filmy'),
    url(r'^krystian/$', views.krystian, name='krystian'),
    url(r'^search/$', views.search, name='search'),
)
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
