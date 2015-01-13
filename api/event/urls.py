import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'event/$', views.EventUploadListView.as_view(), name='event-upload-list'),
)