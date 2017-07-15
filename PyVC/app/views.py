"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required

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
        }
    )

@login_required
def profile(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/profile.html',
        )

@login_required
def modify_password(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user/settings/password.html',
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
