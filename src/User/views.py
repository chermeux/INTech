from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, "User/login.html")

@login_required(login_url='presentation')
def logout(request):
    return render(request, "User/logout.html")

@admin.register()
def signin(request):
    return render(request, "User/signin.html")
