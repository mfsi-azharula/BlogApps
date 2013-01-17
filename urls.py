from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
import os.path
#admin.autodiscover()

urlpatterns = patterns('',
    
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('blog.urls', namespace="blog")),
	( r'^static/(?P<path>.*)$', 'django.views.static.serve', 
    { 'document_root': os.path.join(os.path.dirname(__file__), 'media').replace('\\','/') } ),)
