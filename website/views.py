from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext

def index(request):
    template = loader.get_template('website/index.html')
    context = RequestContext(request)
    return render(request, 'website/index.html')


@ensure_csrf_cookie
def gate(request):
    return render_to_response('website/gate.html')


def check(request):
    if request.method == 'POST':
        if request.POST.get('373,325') == '153,0,0' and \
                request.POST.get('379,352') == '153,76,0' and \
                request.POST.get('316,369') == '153,153,0' and \
                request.POST.get('254,528') == '76,0,153' and \
                request.POST.get('303,469') == '153,0,76' and \
                request.POST.get('327,505') == '153,0,76' and \
                request.POST.get('305,528') == '152,0,153':
                    request.session['passport_board'] = True
                    return HttpResponse('board')

    return HttpResponse('no where to go')
