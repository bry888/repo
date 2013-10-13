from django.conf.urls import patterns, url
#from django.contrib.auth.views import login, logout

from main_app import views

#Generic vievs:
urlpatterns = patterns('',
    url(r'^$', views.MainView.as_view(), name='main_view'),
    url(r'^login/$', views.login_view, name='login', {'template_name':'main_app/login.html', 'redirect_field_name':'main_app.user_view'}),
    url(r'^register/$', views.register_view, name='register', {'template_name':'main_app/register.html', 'redirect_field_name':'main_app.user_view'})),
    url(r'^(?P<pk>\w+)/$', views.UserView.as_view(), name='user_view'),
    url(r'^(?P<pk>\w+)/(?P<pk>\w+)/$', views.ArticleDetailView.as_view(), name='article'),
    #url(r'^accounts/login/$', login),
    #url(r'^accounts/logout/$', logout),
                       # template at: registration/login.html
)
