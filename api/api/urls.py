from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
	url(r'^', include('username.urls')),
	#url(r'^', include('gscondominiums.urls')),
	#url(r'^user/', include('gsuser.urls')),
)
