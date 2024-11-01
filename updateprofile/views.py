from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserForm,ProfilePicForm
from accounts.models import CustomUser
def sample_home(request,pk):
    users = users = get_object_or_404(CustomUser, pk=pk) 
    return render(request, 'home.html', {'users': users})

def sample(request):
    return render(request,'sample.html')

def user_list(request,pk):
    users = users = get_object_or_404(CustomUser, pk=pk) 
    return render(request, 'user_profile.html', {'users': users})

def update_user(request, pk):
    users = get_object_or_404(CustomUser, pk=pk) 
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES or None, instance=users)
        if form.is_valid(): 
            form.save()
            return redirect('profile:user_profile',pk=users.pk)  
    else:
        form = UserForm(instance=users)  
    return render(request, 'update_profile.html', {'users': users, 'form': form})
