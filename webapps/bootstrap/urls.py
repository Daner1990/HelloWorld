#!/usr/bin/env python

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('bootstrap.views',
    url(r'^/$', 'base', name="bootstrap_base"),
    url(r'^base/$', TemplateView.as_view(template_name='bootstrap/base.html')),
)
