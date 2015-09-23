from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


def passport_required(name):
    def _func(func):
        def __func(request, *args, **kwargs):
            if not request.session.get('passport_'+name):
                return HttpResponseRedirect(reverse('website:gate'))
            return func(request, *args, **kwargs)
        return __func
    return _func
