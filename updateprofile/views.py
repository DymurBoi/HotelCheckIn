from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from accounts.models import CustomUser
from sortingroom.models import Reservation,Room
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
        form = UserForm(request.POST, request.FILES, instance=users)  # Corrected line
        if form.is_valid():
            form.save()
            return redirect('profile:user_profile', pk=users.pk)  
        else:
            print(form.errors)  # Debugging form errors
    else:
        form = UserForm(instance=users)

    return render(request, 'update_profile.html', {'users': users, 'form': form})

def reservation_list(request,pk):
    user_logged=get_object_or_404(CustomUser,pk=pk)
    reservation=Reservation.objects.filter(user=user_logged)
    context={
        'user':user_logged,
        'reservations':reservation
    }
    return render(request,'reservations_list.html',context)

def room_view(request,pk):
    user_logged=get_object_or_404(CustomUser,pk=pk)
    reservation=get_object_or_404(Reservation,user=user_logged)
    context={
        'user':user_logged,
        'reservation':reservation
    }
    if request.method=='POST':
        room = get_object_or_404(Room, pk=reservation.room.pk)
        if room.room_check_in==True:
            room.room_check_in = False
            room.save()
        elif room.room_check_in==False:
            room.room_check_in = True
            room.save()
        return redirect('profile:room_view',pk=user_logged.pk)
    return render(request,'room.html',context)
