"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth
from django.contrib.auth.hashers import make_password

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        context = 
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'PageName':'home',
        }
    )

@login_required
def profile(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/profile.html',
        {'PageName':'profile'},
        )

@login_required
def dashboard(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/dashboard/dashboard.html',
        {'PageName':'dashboard'},
        )

@login_required
def issues(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/dashboard/issues.html',
        {'PageName':'issues'},
        )

@login_required
def pulls(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/dashboard/issues.html',
        {'PageName':'pulls'},
        )

@login_required
def explore(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/explore/repos.html',
        {'PageName':'explore'},
        )

@login_required
def explore_organization(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/explore/organizations.html',
        {'PageName':'explore_organization'},
        )

@login_required
def explore_users(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/explore/users.html',
        {'PageName':'explore_users'},
        )

@login_required
def modify_password(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/settings/password.html',
        )

@login_required
def modify_password_post(request):
    assert isinstance(request, HttpRequest)
    msg = ""
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        password = request.POST.get('password')
        retype = request.POST.get('retype')
        result = request.user.check_password(old_password)
        if request.user.is_active and result and str(password) == str(retype):
            request.user.set_password(retype)
            request.user.save()
            msg = "密码修改成功！"
        elif result and str(password) != str(retype):
            msg = "新密码输入不一致！"
        else:
            msg = "密码修改失败"

    return render(
        request,
        'app/user/settings/password.html',
        { "msg" : msg },
        )

@login_required
def modify_email_post(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/settings/email.html',
        { },
        )
    
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context = {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context = {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
