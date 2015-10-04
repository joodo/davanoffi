from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^gate/$', views.gate, name='gate'),
    url(r'^gate/check/$', views.check, name='check'),
    url(r'^loveletter/$', views.loveletter, name='loveletter'),
)
