from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from accounts.models import CustomUser
from sortingroom.models import Reservation
from dashboard.models import Room
def sample_home(request,pk):
    users = users = get_object_or_404(CustomUser, pk=pk) 
    return render(request, 'updateprofile/home.html', {'users': users})

def sample(request):
    return render(request,'updateprofile/sample.html')

def user_profile(request):
    pk=request.session.get('pk')
    users = users = get_object_or_404(CustomUser, pk=pk) 
    return render(request, 'updateprofile/user_profile.html', {'users': users})

def update_user(request):
    pk=request.session.get('pk')
    users = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=users)  # Corrected line
        if form.is_valid():
            form.save()
            request.session['profile_pic']=users.profile_pic.url
            request.session['firstname']=users.firstname
            request.session['lastname']=users.lastname
            return redirect('profile:user_profile')  
        else:
            print(form.errors)  # Debugging form errors
    else:
        form = UserForm(instance=users)

    return render(request, 'updateprofile/update_profile.html', {'users': users, 'form': form})

def reservation_list(request):
    pk=request.session.get('pk')
    user_logged=get_object_or_404(CustomUser,pk=pk)
    reservation=Reservation.objects.filter(email=user_logged.username)
    context={
        'user':user_logged,
        'reservations':reservation
    }
    return render(request,'updateprofile/reservations_list.html',context)

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect('account:login')
