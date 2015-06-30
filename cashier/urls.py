from django.conf.urls import patterns, url

from cashier import views

urlpatterns = patterns('',
                       url(r'^$', views.cashier_list, name='cashier_list'),
                       url(r'^new$', views.cashier_create, name='cashier_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.cashier_update, name='cashier_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.cashier_delete, name='cashier_delete'),
)