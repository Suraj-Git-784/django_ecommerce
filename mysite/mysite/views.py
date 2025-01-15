from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello')

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse('Capitalize this')