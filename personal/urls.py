from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('staticpages.urls', namespace='staticpages')),
)
