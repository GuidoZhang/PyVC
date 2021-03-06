﻿"""
Definition of urls for PyVC.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
import django
from app import views
import django.contrib.auth.views as djAuthView
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),
    url(r'^login/$',
        djAuthView.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        djAuthView.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^profile$',
        views.profile,
        {},
        name='profile'),

    url(r'^dashboard$',
        views.dashboard,
        {},
        name='dashboard'),

    url(r'^issues$',
        views.issues,
        {},
        name='issues'),

    url(r'^explore$',
        views.explore,
        {},
        name='explore'),

    url(r'^explore/organization$',
        views.explore_organization,
        {},
        name='explore_organization'),

    url(r'^explore/users$',
        views.explore_users,
        {},
        name='explore_users'),

    url(r'^pulls',
        views.pulls,
        {},
        name='pulls'),

    url(r'^profile/modify/password$',
        views.modify_password,
        {},
        name='modify_password'),

    url(r'^profile/modify/password_post$',
        views.modify_password_post,
        {},
        name='modify_password_post'
        ),

    url(r'^profile/modify/email$',
        views.modify_email_post,
        {},
        name='modify_email_post'
        ),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]
