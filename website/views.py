from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext

from utils.passport import passport_required

def index(request):
    template = loader.get_template('website/index.html')
    context = RequestContext(request)
    return render(request, 'website/index.html')


@ensure_csrf_cookie
def gate(request):
    return render_to_response('website/gate.html')


def check(request):
    BOARD_LOCK = {'373,325': '153,0,0',
                  '379,352': '153,76,0',
                  '316,369': '153,153,0',
                  '254,528': '76,0,153' ,
                  '303,469': '153,0,76' ,
                  '327,505': '153,0,76' ,
                  '305,528': '152,0,153',
    }
    LOVELETTER_LOCK = {'182,520': '0,153,0',
                       '184,393': '0,153,0',
    }

    if request.method == 'POST':
        if is_fit(request.POST, BOARD_LOCK):
            request.session['passport_board'] = True
            return HttpResponse('board')

        if is_fit(request.POST, LOVELETTER_LOCK):
            request.session['passport_loveletter'] = True
            return HttpResponse('loveletter')

    return HttpResponse('no where to go')


@passport_required('loveletter')
def loveletter(request):
    return render(request, 'website/loveletter.html')


def is_fit(key, lock):
    for k, v in lock.items():
        if key.get(k) != v:
            print(key.get(k))
            print(v)
            return False
    return True
