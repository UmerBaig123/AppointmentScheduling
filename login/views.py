from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confpassword = request.POST['confirmpassword']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is taken')
            return redirect('register')
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long')
            return redirect('register')
        if password != confpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'User created successfully')
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')