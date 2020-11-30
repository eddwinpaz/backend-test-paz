from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


def login_required(f):
    def wrap(request, *args, **kwargs):
        # this check the session if userid key exist, if not it will redirect to login page
        if 'userId' not in request.session.keys():
            return HttpResponseRedirect("/user/login/")
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


def admin_required(f):
    def wrap(request, *args, **kwargs):
        # this check the session if userid key exist, if not it will redirect to login page
        if 'isAdmin' not in request.session.keys():
            raise PermissionDenied
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
