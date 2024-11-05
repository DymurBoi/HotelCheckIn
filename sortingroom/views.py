from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Room, Reservation
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.

def room_list(request):
    sort_by = request.GET.get('sort_by', 'room_type')
    
    valid_sort_fields = ['room_type', 'room_price', 'rooms_available']
    if sort_by not in valid_sort_fields:
        sort_by = 'room_type' 

    if sort_by == 'rooms_available':
        rooms = Room.objects.all().order_by('-rooms_available')
    else:
        rooms = Room.objects.all().order_by(sort_by) 

    return render(request, 'sortingroom/room_list.html', {'rooms': rooms})


def reserve_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        # Extract data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        special_request = request.POST.get('special_request')
        user=get_object_or_404(CustomUser,username=email)
        # Save the reservation
        reservation = Reservation(
            room=room,
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            phone=phone,
            check_in=check_in,
            check_out=check_out,
            special_request=special_request
        )
        reservation.save()

        # Calculate the total cost
        stay_duration = (datetime.strptime(check_out, "%Y-%m-%d").date() - 
                         datetime.strptime(check_in, "%Y-%m-%d").date()).days
        total_cost = stay_duration * float(room.room_price)

        # Redirect to the payment page with reservation_id and total_cost
        return redirect('sort:payment_page', reservation_id=reservation.id, total_cost=total_cost)

    return render(request, 'sortingroom/reserve_room.html', {'room': room})




def payment_page(request, reservation_id, total_cost):
    reservation = Reservation.objects.get(id=reservation_id)
    total_cost = float(total_cost)

    formatted_total_cost = f"{total_cost:.2f}" 
    
    context = {
        'reservation': reservation,
        'total_cost': formatted_total_cost,
    }
    return render(request, 'sortingroom/payment.html', context)
