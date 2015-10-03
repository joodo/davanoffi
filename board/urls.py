from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.PostAll.as_view(), name='index'),
    url(r'^tag/(?P<tag>.+?)/$', views.PostInTag.as_view(), name='tag'),
    url(r'^loveletter/$', views.loveletter, name='loveletter'),
    url(r'^new/$', views.PostCreateView.as_view(), name='new'),
)
