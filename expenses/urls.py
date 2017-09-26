from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dwelling_id>[0-9]+)/room/add/$', views.room_add, name='room_add'),
    url(r'^(?P<room_id>[0-9]+)/appliance/add/$', views.appliance_add, name='appliance_add'),
    url(r'^(?P<appliance_id>[0-9]+)/electricity_usage/add/$', views.electricity_usage_add, name='electricity_usage_add'),
    url(r'^(?P<appliance_id>[0-9]+)/water_usage/add/$', views.water_usage_add, name='water_usage_add'),
    url(r'^room/delete/(?P<pk>\d+)/$', views.RoomDelete.as_view(), name="room_delete"),
    url(r'^appliance/delete/(?P<pk>\d+)/$', views.ApplianceDelete.as_view(), name="appliance_delete"),
    url(r'^electricity_usage/delete/(?P<pk>\d+)/$', views.ElectricityUsageDelete.as_view(), name="electricity_usage_delete"),
    url(r'^water_usage/delete/(?P<pk>\d+)/$', views.WaterUsageDelete.as_view(), name="water_usage_delete"),
    url(r'^(?P<dwelling_id>[0-9]+)/$', views.dwelling_detail, name='dwelling_detail'),
    url(r'^(?P<dwelling_id>[0-9]+)/update/$', views.dwelling_update, name='dwelling_update'),
]