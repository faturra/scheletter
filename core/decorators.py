from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from core import config

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def group_required(*group_names):
    """
    Decorator untuk membatasi akses halaman hanya untuk pengguna dengan grup yang sesuai.
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=group_names).exists() or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'handlers/access_denied.html')
        return wrapper
    return decorator

def opr_required(view_func):
    """
    Decorator untuk membatasi akses halaman hanya untuk pengguna dengan grup 'operator'.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name=config.opr).exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'handlers/access_denied.html')
    
    return wrapper

def prl_required(view_func):
    """
    Decorator untuk membatasi akses halaman hanya untuk pengguna dengan grup 'operator'.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name=config.prl).exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'handlers/access_denied.html')
    
    return wrapper

def hoa_required(view_func):
    """
    Decorator untuk membatasi akses halaman hanya untuk pengguna dengan grup 'operator'.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name=config.hoa).exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'handlers/access_denied.html')
    
    return wrapper

def scs_required(view_func):
    """
    Decorator untuk membatasi akses halaman hanya untuk pengguna dengan grup 'operator'.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name=config.scs).exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'handlers/access_denied.html')
    
    return wrapper

def ecs_required(view_func):
    """
    Decorator untuk membatasi akses halaman hanya untuk pengguna dengan grup 'operator'.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name=config.ecs).exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'handlers/access_denied.html')
    
    return wrapper