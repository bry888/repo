from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brybak_rss.views.home', name='home'),
    # url(r'^brybak_rss/', include('brybak_rss.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^main_app/', include('main_app.urls', namespace="main_app")),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
