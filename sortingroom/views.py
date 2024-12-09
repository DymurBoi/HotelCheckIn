from pyexpat.errors import messages
from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from django.utils import timezone
from django.utils.timezone import now
from .models import Reservation, Payment
from dashboard.models import RoomCategory, Room
from accounts.models import CustomUser
from .forms import ReservationForm

# Create your views here.

def room_category(request):
    # Get the currently logged-in user
    sort_by = request.GET.get('sort_by', 'category_id')
    pk=request.session.get('pk')
    users = users = get_object_or_404(CustomUser, pk=pk) 
    if sort_by == 'rooms_available':
        room_category = sorted(
            RoomCategory.objects.all(),
            key=lambda category: category.rooms_available,
            reverse=True
        )
    else:
        valid_sort_fields = ['category_id', 'room_price']
        if sort_by not in valid_sort_fields:
            sort_by = 'category_id'
        room_category = RoomCategory.objects.all().order_by(sort_by)

    return render(request, 'sortingroom/room_list.html', {
        'room_category': room_category,
        'users': users
    })

def reserve_room(request, roomId):
    pk = request.session.get('pk')
    users = get_object_or_404(CustomUser, pk=pk)
    room_category = get_object_or_404(RoomCategory, id=roomId)
    available_room = Room.objects.filter(room_category=room_category, is_available=True).first()

    if not available_room:
        return render(request, 'sortingroom/no_rooms_available.html', {'users': users})

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = available_room
            reservation.save()

            # Calculate total cost
            stay_duration = (reservation.check_out - reservation.check_in).days
            total_cost = stay_duration * float(room_category.room_price)

            # Create a payment instance
            payment = Payment(
                reservation=reservation,
                payment_total=total_cost,
                payment_status="Pending"
            )
            payment.save()

            return redirect('sortingroom:payment_page', reservation_id=reservation.id, total_cost=total_cost)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ReservationForm()

    return render(request, 'sortingroom/reserve_room.html', {
        'room': available_room,
        'form': form,
        'users': users
    })
def payment_page(request, reservation_id, total_cost):
    users = request.user
    reservation = get_object_or_404(Reservation, id=reservation_id)
    formatted_total_cost = f"{float(total_cost):.2f}"

    if request.method == 'POST':
        # Process payment (mocked here as successful)
        reservation.room.is_available = False
        reservation.room.save()

        # Update payment status to "Paid"
        payment = Payment.objects.get(reservation=reservation)
        payment.payment_status = "Paid"
        payment.payment_method = request.POST.get('payment-method')
        payment.payment_date = timezone.now().date() 
        payment.save()

        # Redirect to the payment confirmed page
        return redirect('sortingroom:payment_confirmed', payment_id=payment.id)

    return render(request, 'sortingroom/payment.html', {
        'users': users,
        'reservation': reservation,
        'total_cost': formatted_total_cost,
    })

def payment_confirmed(request, payment_id):
    users = request.user
    payment = get_object_or_404(Payment, id=payment_id)
    reservation = payment.reservation

    return render(request, 'sortingroom/payment_confirmed.html', {
        'users': users,
        'reservation': reservation,
        'payment': payment,
    })
    
def about(request):
    pk=request.session.get('pk')
    users = users = get_object_or_404(CustomUser, pk=pk) 
    return render(request, 'sortingroom/about.html', {'users': users} )