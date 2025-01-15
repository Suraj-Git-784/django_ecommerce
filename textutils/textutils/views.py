from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'harry', 'place': 'Mars'}
    return render(request, 'index.html', params)
    # return HttpResponse('Hello')

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse('Capitalize this')