from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('website.urls', namespace='website')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
