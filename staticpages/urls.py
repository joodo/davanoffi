from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from staticpages import views

urlpatterns = patterns('',
                       #url(r'^$', TemplateView.as_view(template_name="staticpages/index.html")),
                       url(r'^$', views.index, name='index'),
                       url(r'^secret/$', views.secret, name='secret'),
                       url(r'^happy/$', views.happy, name='happy'),
)
