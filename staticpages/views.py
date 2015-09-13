from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext

def index(request):
    template = loader.get_template('staticpages/index.html')
    context = RequestContext(request)
    return render(request, 'staticpages/index.html')

def secret(request):
    return render(request, 'staticpages/secret.html')

def happy(request):
    return render(request, 'staticpages/happy.html')
