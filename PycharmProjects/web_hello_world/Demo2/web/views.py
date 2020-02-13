from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    s = 'Hello World!'
    #current_time = datetime.datetime.now()
    current_time = '2019-03-20'
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)
