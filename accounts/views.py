from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')  # Redirect to login after successful signup
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Debugging statements
            print("Username:", username)  # Prints the username entered
            print("Password Attempt:", password)  # Prints the password entered
            
            try:
                user = CustomUser.objects.get(username=username)
                if user.check_password(password):  # Use check_password method
                    login(request, user)
                    request.session['pk']=user.pk
                    request.session['profile_pic']=user.profile_pic.url
                    request.session['firstname']=user.firstname
                    request.session['lastname']=user.lastname
                    return redirect('sortingroom:room_category')  # Redirect to the homepage
                else:
                    form.add_error(None, 'Invalid username or password')
            except CustomUser.DoesNotExist:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomUserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def HomePageView(request):
    return render(request, 'base/landingpage.html') 

@login_required
def SuccessPageView(request):
    return render(request, 'accounts/success.html')
