import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'users/$', views.UserRegisterView.as_view(), name='user-register'),
)