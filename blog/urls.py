from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^index/(?P<tag>.+?)/$', views.index, name='index'),
                       url(r'^loveletter/$', views.loveletter, name='loveletter'),
                       url(r'^post/$', views.post, name='post'),
                       url(r'^new/$', views.new, name='new'),
)
