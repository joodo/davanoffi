from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^addproject/$', views.addproject, name='addproject'),
                       url(r'^removeschedule/(?P<schedule_id>\d+)/$', views.removeschedule, name='removeschedule'),
                       url(r'^(?P<project_id>\d+)/$', views.project, name='project'),
                       url(r'^(?P<project_id>\d+)/manual/$', views.manual, name='manual'),
                       url(r'^(?P<project_id>\d+)/detail/$', views.detail, name='detail'),
                       url(r'^(?P<project_id>\d+)/addschedule/$', views.addschedule, name='addschedule'),
                       url(r'^(?P<project_id>\d+)/removeproject/$', views.removeproject, name='removeproject'),
)
