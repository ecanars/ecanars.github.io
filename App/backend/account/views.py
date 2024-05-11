import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from profiles.models import UserProfile

from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request,username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render (request, "account/login.html", {"error":"username ya da parola yanlış"})
    else:
        return render(request, "account/login.html")


def user_register(request):
    if request.method == "POST":
        name = request.POST["name"]
        department = request.POST["department"]
        year = request.POST["year"]
        id_number = request.POST["id_number"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        role = request.POST["role"]  # Capture the role from the form

        if password == repassword:
            if User.objects.filter(email=email).exists():
                return render(request, "account/register.html", {"error": "Email already in use", "username": username, "email": email})
            elif User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "Username already in use", "username": username, "email": email})
            else:
                if role == 'admin':  # Check if the selected role is 'admin'
                    user = User.objects.create_user(username=username, email=email, password=password, is_superuser=True, is_staff=True)
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    group = Group.objects.get(name=role)  # Retrieve the group for the role
                    user.groups.add(group)  # Add the user to the group
                    userProfile = UserProfile.create(user, id_number, name, email, department, year)
                    userProfile.save()
                
                user.save()
                login(request, user)  # Optionally log the user in after registering
                return redirect("index")  # Redirect to the homepage
        else:
            return render(request, "account/register.html", {"error": "Passwords do not match", "username": username, "email": email})

    return render(request, "account/register.html", {'active_page': 'register'})
def user_logout(request):
    logout(request)
    return redirect("user_login")

def users(request):
    return render(request, 'pages/users.html', {'active_page': 'users'})


