from django.conf.urls import patterns, url

from transaction import views

urlpatterns = patterns('',
                       url(r'^$', views.transaction_list, name='transaction_list'),
                       url(r'^new$', views.transaction_create, name='transaction_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.transaction_update, name='transaction_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.transaction_delete, name='transaction_delete'),
)