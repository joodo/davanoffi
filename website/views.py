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
    BOARD_LOCK = {"94,101":"153,0,76",
            "120,75":"153,0,76",
            "126,73":"153,0,76",
            "409,42":"153,0,76",
            "401,48":"153,0,76",
            "444,56":"153,0,76",
            "210,568":"76,0,153",
            "327,573":"76,0,153",
            "242,203":"0,153,76",
            "325,176":"153,0,0"}
    LOVELETTER_LOCK = {"271,292":"153,0,76",
            "382,293":"153,0,76",
            "373,325":"152,0,153",
            "316,369":"76,0,153",
            "273,413":"0,76,153",
            "301,447":"0,0,153"}

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
