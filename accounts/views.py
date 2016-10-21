from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
from rest_framework.views import APIView


# Create your views here.

def login_view(request):
    if request.user.is_authenticated():
        return redirect('/quiz/')

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('/quiz/')
    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated():
        return redirect('/quiz/')

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        final_user = authenticate(
            username=user.username, password=password)
        login(request, final_user)
        return redirect('/quiz/')

    return render(request, "accounts/register.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')
