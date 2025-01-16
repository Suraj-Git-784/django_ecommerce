from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Hello')

def analyze(request):
    djtext = request.GET.get('analyze', 'default')
    print(djtext)
    analyzed = djtext
    params = {'purpose': 'Remove Punctuation', 'analyzed_text' : analyzed}
    return render(request, 'analyze.html', params)

def capfirst(request):
    return HttpResponse('Capitalize this')