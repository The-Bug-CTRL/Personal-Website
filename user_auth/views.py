from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:show_user')  # Redirect to a profile page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user_auth:show_user'))
        else:
            # Handle unsuccessful login, perhaps render the login form again with an error message
            return render(request, 'authentication/login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'authentication/login.html')

def show_user(request):
    # Avoid displaying or logging the user's password for security reasons
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
    })

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_auth:login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})






