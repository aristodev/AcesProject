# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.shortcuts import render
from .form import RegisterForm, loginForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout



# Create your views here.
@login_required
def Home(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        phone = request.user.phone
        email = request.user.email
    context = {
        'username': username,
        'phone' : phone,
        'email': email
    }
    return render(request, "home.html", context)




def not_loggedin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/home') # redirect to profile page
        else:
            return function(request, *args, **kwargs)
    return wrap

@not_loggedin_required
def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned(normalized) data
            #username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            user.set_password(password)
            user.save()

            return redirect('/login')
        else:
            return render(request, 'register.html', {'form': form})

    else:
        context = {
            'form': RegisterForm
        }
        return render(request, "register.html", context)
