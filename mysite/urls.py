from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'^', include('blog.urls')),
	url(r'^latestnews/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', include('haystack.urls')),
    )
