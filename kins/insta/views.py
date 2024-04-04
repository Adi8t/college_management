from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login as auth_login



def home(request):
    return render(request, "home.html")

 
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def logout1(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request, "hodsirpanel.html")


def signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cnfrm_password = request.POST.get("confirm_password")
        date_of_birth = request.POST.get("dateofbirth")

        
        if User.objects.filter(email=email).exists():
            context = {
                "error_message": "Email already exists."
            }
            return render(request, 'signup.html', context=context)

        if password == cnfrm_password:
            
            user, created = User.objects.get_or_create(email=email, username=name, date_of_birth=date_of_birth)
            if created:
                user.set_password(password)  
                user.save()
                login(request,user)
                return redirect('home')
        else:
            context = {
                "error_message": "Passwords do not match."
            }
            return render(request, 'signup.html', context=context)
    else:
        return render(request, 'signup.html')