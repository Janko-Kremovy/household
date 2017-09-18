from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dwelling_id>[0-9]+)/room/add/$', views.room_add, name='room_add'),
    url(r'^(?P<room_id>[0-9]+)/appliance/add/$', views.appliance_add, name='appliance_add'),
    url(r'^room/delete/(?P<pk>\d+)/$', views.RoomDelete.as_view(), name="room_delete"),
    url(r'^(?P<dwelling_id>[0-9]+)/$', views.dwelling_detail, name='dwelling_detail'),
    url(r'^(?P<dwelling_id>[0-9]+)/update/$', views.dwelling_update, name='dwelling_update'),
]