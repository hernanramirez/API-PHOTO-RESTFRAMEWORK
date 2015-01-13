from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('username.urls')),
	url(r'^', include('event.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
