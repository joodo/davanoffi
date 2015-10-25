from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.PostAll.as_view(), name='index'),
    url(r'^tag/(?P<pk>.+?)/setting/$', views.TagSettingView.as_view(), name='tag_setting'),
    url(r'^tag/(?P<tag>.+?)/$', views.PostInTag.as_view(), name='tag'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/(?P<tag>.+?)/$', views.PostDetailView.as_view(), name='detail_with_tag'),
    url(r'^new/$', views.PostCreateView.as_view(), name='new'),
)
