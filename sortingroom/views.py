from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from django.utils import timezone
from django.utils.timezone import now
from .models import Reservation, Payment
from dashboard.models import RoomCategory, Room
from accounts.models import CustomUser


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
    pk=request.session.get('pk')
    users = users = get_object_or_404(CustomUser, pk=pk) 
    room_category = get_object_or_404(RoomCategory, id=roomId)
    available_room = Room.objects.filter(room_category=room_category, is_available=True).first()

    if not available_room:
        return render(request, 'sortingroom/no_rooms_available.html', {'users': users})

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

        # Validate the dates
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
            today = now().date()

            if check_in_date < today:
                raise ValidationError("Check-in date must be today or later.")
            if check_in_date >= check_out_date:
                raise ValidationError("Check-in date must be before the check-out date.")

            # Create the reservation with the available room
            reservation = Reservation(
                room=available_room,
                first_name=first_name,
                last_name=last_name,
                email=email,
                country=country,
                phone=phone,
                check_in=check_in_date,
                check_out=check_out_date,
                special_request=special_request
            )

            reservation.full_clean()  # Validate the reservation instance
            reservation.save()

            # Calculate total cost
            stay_duration = (check_out_date - check_in_date).days
            total_cost = stay_duration * float(room_category.room_price)

            # Create a payment instance
            payment = Payment(
                reservation=reservation,
                payment_total=total_cost,
                payment_status="Pending"
            )
            payment.save()

            # Redirect to payment page
            return redirect('sortingroom:payment_page', reservation_id=reservation.id, total_cost=total_cost)

        except ValidationError as e:
            # Handle validation errors
            return render(request, 'sortingroom/reserve_room.html', {
                'room': available_room,
                'errors': e.messages,
                'input_data': request.POST
            })
        except ValueError:
            # Handle date parsing errors
            return render(request, 'sortingroom/reserve_room.html', {
                'room': available_room,
                'errors': ["Invalid date format. Please enter dates in YYYY-MM-DD format."],
                'input_data': request.POST
            })

    return render(request, 'sortingroom/reserve_room.html', {'room': available_room, 'users': users})

def payment_page(request, reservation_id, total_cost):
    users = request.user
    reservation = get_object_or_404(Reservation, id=reservation_id)
    formatted_total_cost = f"{float(total_cost):.2f}"

    if request.method == 'POST':
        # Process payment (mocked here as successful)
        reservation.room.is_reserved = True
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
