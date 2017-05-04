from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    a = request.GET['a'].encode('utf-8')
    b = request.GET['b'].encode('utf-8')
    res_str = str.format("".encode('utf-8'))
                         # , b = %s, a + b = %s' % (str(a), str(b), '1'))
    return HttpResponse('hello world\n' + res_str)

def test(request):
    a = request.GET['a']
    b = request.GET['b']
    print 'test' + a
    res_str = ''
    res_str = str.format('a= %d' % int(1))
    return HttpResponse('hheheh' + res_str)
# Create your views here.
