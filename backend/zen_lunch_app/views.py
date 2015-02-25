from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms import SignupForm
from zen_lunch_app.models import User

def home(request):
    success=None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            success = "Thanks for signing up!"
            form = SignupForm()
    else:
        form = SignupForm()
    return render(request, 'home.html', {
        'form': form,
        'success': success
    })
    #                          context_instance=RequestContext(request))


def signups(request):
    return HttpResponse(User.objects.count())
