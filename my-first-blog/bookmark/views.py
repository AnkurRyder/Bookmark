from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from bookmark.models import Data




def dashboard(request):
    if request.user.is_authenticated():
        data=request.user.data_set.all()
        return render(request, 'bookmark/dashboard.html',{'data':data})
    else:
        return redirect('signin')

def signin(request):

    return render(request, 'bookmark/signin.html')

def logedin(request):
    return render(request, 'bookmark/logedin.html')

def verify(request):
    #email_id = request.GET.get('email_id', None)
    email_id = request.POST.get('email_id',None)
    name = request.POST.get('name',None)

    try:
        User.objects.get(username = email_id)
    except:
        register(request)

    else:
        user = authenticate(username= email_id, password='.swillconnect')
        login(request, user)
        lamda=User.objects.get(username = email_id)
        lamda.last_name=name
        lamda.save()
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
         return redirect('dashboard')
    else:

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('dashboard')

        else:
            form = UserCreationForm()
        return render(request, 'bookmark/signuppl.html', {'form': form})


def register(request):
    email_id = request.POST.get('email_id',None)
    name = request.POST.get('name',None)
    user=User.objects.create_user(username = email_id, password='.swillconnect',last_name=name);
    user.save()
    login(request, user)
    data = {
            'is_verified': False
        }
    return JsonResponse(data)


def add(request):
    if request.method == 'POST':

        #u = User.objects.get(username=r'ms27@iitbbs.ac.in')
        title = request.POST.get("title", None)
        url = request.POST.get("ur", None)
        tag = request.POST.get("tag", None)


        u = request.user
        c = Data(user=u,title=title, url=url, pub_date=timezone.now())
        #c.user = u
        c.save()
        data = {
                'no_of_bookmarks': 10,
            }
        return JsonResponse(data)


    else: return render(request, 'bookmark/add.html')

def user(request):
    return render(request, 'bookmark/user.html')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(first_name__iexact=username).exists()
    }
    return JsonResponse(data)

def welcome(request):
    return render(request, 'bookmark/welcome.html')

def delete_bookmark(request):
    pk = request.POST.get("pk", None)
    Data.objects.get(pk=pk).delete()
    data = {
        'success': True
    }
    return JsonResponse(data)

def update_frequency(request):
    pk = request.POST.get("pk", None)
    bookmark = Data.objects.get(pk=pk)
    bookmark.freq = bookmark.freq + 1
    bookmark.save()
    data = {
            'succes': True
        }
    return JsonResponse(data)



def add_get(request):

    #u = User.objects.get(username=r'ms27@iitbbs.ac.in')
    title = request.GET.get("title", None)
    url = request.GET.get("ur", None)
    tag = request.GET.get("tag", None)


    u = request.user
    c = Data(user=u,title=title, url=url, pub_date=timezone.now())
    #c.user = u
    c.save()
    data = {
            'no_of_bookmarks': 10,
        }
    return JsonResponse(data)


def extension_check(request):
    return render(request, 'bookmark/extension_check.html')













