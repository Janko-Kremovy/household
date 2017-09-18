from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dwelling_id>[0-9]+)/room/add/$', views.room_add, name='room_add'),
    url(r'^(?P<dwelling_id>[0-9]+)/$', views.dwelling_detail, name='dwelling_detail'),
    url(r'^(?P<dwelling_id>[0-9]+)/update/$', views.dwelling_update, name='dwelling_update'),
]