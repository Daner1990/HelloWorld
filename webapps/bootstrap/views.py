#!/usr/bin/python
#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def base(request, template_name="bootstrap/base.html"):
    """
    """
    return render_to_response(template_name, RequestContext(request))

