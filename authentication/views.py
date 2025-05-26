from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages 
from django.db import IntegrityError

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            messages.success(request,"Account creation successful")
            return redirect("login_page")
        except IntegrityError as e:
            messages.error(request,f"Error occured : {e}")
            return render(request,'signup.html')   
    return render(request,'signup.html')




def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect('dashboard')
        messages.error(request,"Invalid Login Credential")
        return render(request,"login.html")
    return render(request,"login.html")



def dashboard(request):
    return render(request,"dashboard.html")