from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from forms import Registration_form, Authenticate_form
# Create your views here.
def login(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = authenticate(email=email, password=password)
    if user is not None and user.is_active:
        django_login(request, user)
        return redirect(reverse('dashboard'))

    return render_to_response('accounts/login.html', locals(), context_instance = RequestContext(request))

def register(request):

    if request.method == 'POST':
        form = Registration_form(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect(reverse('login'))
    else:
        form = Registration_form()
    return render_to_response('accounts/register.html', locals(), context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect(reverse('login'))