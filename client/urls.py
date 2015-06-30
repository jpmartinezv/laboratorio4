from django.conf.urls import patterns, url

from client import views

urlpatterns = patterns('',
                       url(r'^$', views.client_list, name='client_list'),
                       url(r'^new$', views.client_create, name='client_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.client_update, name='client_edit'),
                       url(r'^profile/(?P<pk>\d+)$', views.client_profile, name='client_profile'),
                       url(r'^delete/(?P<pk>\d+)$', views.client_delete, name='client_delete'),
)