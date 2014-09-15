from django.conf.urls import patterns, url

from superchemik import views

urlpatterns = patterns('',
    url(r'^(?P<page_id>\d+)/$', views.mainpage, name='mainpage'),
    url(r'^komentarze/$', views.comments, name='comments'),
    url(r'^regulamin/$', views.info, name='info'),
    #url(r'^dodaj/$', views.add_comment, name='add_comment'),
)
#    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
