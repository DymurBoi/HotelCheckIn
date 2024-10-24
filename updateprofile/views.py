from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserForm,ProfilePicForm

def sample_home(request):
    return render(request,'home.html')

def sample(request):
    return render(request,'sample.html')

def user_list(request,pk):
    users = users = get_object_or_404(UserProfile, pk=pk) 
    return render(request, 'user_profile.html', {'users': users})

def update_user(request, pk):
    users = get_object_or_404(UserProfile, pk=pk) 
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES or None, instance=users)
        if form.is_valid(): 
            form.save()
            return redirect('user_profile',pk=users.pk)  
    else:
        form = UserForm(instance=users)  
    return render(request, 'update_profile.html', {'users': users, 'form': form})
