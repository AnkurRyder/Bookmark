from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms



def index(request):
    if request.user.is_authenticated():
        data=request.user.data_set.all()
        return render(request, 'bookmark/index.html',{'data':data})
    else:
        return redirect('signin')

def signin(request):

    return render(request, 'bookmark/signin.html')

def logedin(request):
    return render(request, 'bookmark/logedin.html')

def verify(request):
    email_id = request.GET.get('email_id', None)
    #email_id = request.POST.get('email',None)
    print (email_id)
    try:
        User.objects.get(username = email_id)
    except:
        data = {
            'is_verified': False
        }
    else:
        user = authenticate(username= email_id, password='.swillconnect')
        login(request, user)
        data = {
            'is_verified': True
        }

    return JsonResponse(data)

def getting_started(request):
    return render(request, 'bookmark/getting_started.html')

def contact(request):
    return render(request, 'bookmark/contact.html')


def signup(request):

    if request.user.is_authenticated():
         return redirect('index')
    else:

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')

        else:
            form = UserCreationForm()
        return render(request, 'bookmark/signuppl.html', {'form': form})












