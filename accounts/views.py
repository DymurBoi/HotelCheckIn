from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success')  # Redirect to success page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomUserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def HomePageView(request):
    return render(request, 'base/landingpage.html') 

@login_required
def SuccessPageView(request):
    return render(request, 'accounts/success.html')
