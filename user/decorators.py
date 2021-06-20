from django.http import HttpResponse
from django.shortcuts import redirect
from sympy.core.numbers import Half


def allowed_user(allowed_role=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None

            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_role:
                return view_func(request,*args,*kwargs)
            else:
                return HttpResponse("Bạn không được phép truy cập")
        return wrapper_func
    return decorator
