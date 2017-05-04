# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world' )

def test(request):
    a = request.GET['a']
    b = request.GET['b']
    print 'test' + a
    print 'a = {}, b = {}, a+b = {}'.format(a, b, int(a)+int(b))
    res_str = 'a = {}, b = {}, a+b = {}'.format(a, b, int(a)+int(b))
    return HttpResponse('hello world!<br>' + res_str)

def render_test(request):
    # return HttpResponse('hello world!<br>')
    return render(request, 'home.html')
# Create your views here.
