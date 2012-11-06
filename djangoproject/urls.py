from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.defaults import *
from mayday.api import *
from tastypie.api import Api

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(BookResource())
v1_api.register(PersonResource())
v1_api.register(BookCollectionResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^djangoproject/', include('djangoproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)

urlpatterns += staticfiles_urlpatterns()
