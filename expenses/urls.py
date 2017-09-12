from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<dwelling_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<dwelling_id>[0-9]+)/update/$', views.update, name='update'),
]