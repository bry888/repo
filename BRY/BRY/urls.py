from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BRY.views.home', name='home'),
    # url(r'^BRY/', include('BRY.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    #function url( regex-regular expresion , view , kwargs , name) - 2last optional
    url(r'^superchemik/', include('superchemik.urls', namespace="superchemik")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
