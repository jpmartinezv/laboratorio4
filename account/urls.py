from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
                       url(r'^$', views.account_list, name='account_list'),
                       url(r'^new$', views.account_create, name='account_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.account_update, name='account_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.account_delete, name='account_delete'),
)