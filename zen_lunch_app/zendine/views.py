from django.http import HttpResponse
from django.shortcuts import render, redirect

from django import forms
from forms import SignUpForm
from zendine.models import User

def home(request):
    success=None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            success = "Thanks for signing up!"
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'home.html', {
        'form': form,
        'success': success
    })
    #                          context_instance=RequestContext(request))


def signups(request):
    return HttpResponse(User.objects.count())
