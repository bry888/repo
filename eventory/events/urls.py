from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    #url(r'^(?P<year_id>\d+)/(?P<month_id>\d+)/(?P<day_id>\d+)/$', views.mainpage, name='mainpage'),
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^add_event/$', views.add_event, name='add_event'),
)
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
