from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, LightSwitching
from .lightcontrol import LightControler

# Create your views here.

lightControler = LightControler.get_instance()


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/")


def home_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = LightSwitching(request.POST)
            newLightState = 'bedroom' in form.data and form.data['bedroom'] == 'on'
            lightControler.setLightState(newLightState)
            return HttpResponseRedirect("/")
        else:
            form = LightSwitching(
                initial={'bedroom': lightControler.getLightState()})
        return render(request, "home.html", {"form": form})
    else:
        return HttpResponseRedirect("login/")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request, "login.html", {"form": form, "message": "Invalid credentials!"})
        else:
            return HttpResponseRedirect("login/")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form, "message": ""})
