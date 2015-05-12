#!/usr/bin/env python

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bootstrap/', include('bootstrap.urls')),
    url(r'^base/$', TemplateView.as_view(template_name='bootstrap/base.html')),

    url(r'^extension/', TemplateView.as_view(template_name='extension/extension.html')),
)
