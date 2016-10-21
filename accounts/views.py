from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from .forms import UserLoginForm
from rest_framework.views import APIView

# Create your views here.

def login_view(request):
    print(request.user.is_authenticated())
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
    return render(request, "form.html", {})

def logout_view(request):
    logout(request)
    return redirect('/login/')

