from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, RoomCategory
from .forms import RoomForm, CategoryForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from sortingroom.models import Reservation

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:  # Ensure the user is an admin
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('dashboard:admin_landing')
            else:
                messages.error(request, "You are not authorized to access this page.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html')

@login_required
def admin_landing(request):
    admin_id = request.user.id
    username = request.user.username

    booked_room_ids = Room.objects.filter(is_available=False).values_list('id', flat=True)
    # Get all reserved room IDs from reservations
    reserved_room_ids = Reservation.objects.values_list('room_id', flat=True)

    # Exclude rooms that are reserved
    rooms_available = Room.objects.filter(is_available=True).exclude(id__in=reserved_room_ids)

    # Query for booked rooms
    rooms_booked = Room.objects.filter(is_available=False)

    # Fetch all reservations for display
    reservation = Reservation.objects.exclude(room_id__in=booked_room_ids)

    context = {
        'admin_id': admin_id,
        'username': username,
        'rooms_available': rooms_available,
        'rooms_booked': rooms_booked,  
        'reservation': reservation,
    }

    return render(request, 'dashboard/admin_landing.html', context)

def welcome(request):
    return HttpResponse('<h1>Hello</h1>')

@login_required
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Room details updated successfully.")
            return redirect('dashboard:modify_room_landing')
        else:
            messages.error(request, "There was an error updating the room details.")
    else:
        form = RoomForm(instance=room)
    return render(request, 'dashboard/room_detail.html', {'form': form, 'room': room})

@login_required
def add_room(request):
    categories = RoomCategory.objects.all()  # Updated from Category to RoomCategory

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Room added successfully.")
            return redirect('dashboard:admin_landing')
        else:
            messages.error(request, "Error adding room. Please check the form.")
    else:
        form = RoomForm()

    return render(request, 'dashboard/add_room.html', {'form': form, 'categories': categories})

@login_required
def add_or_modify_room(request, room_id=None):
    room = get_object_or_404(Room, id=room_id) if room_id else None

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Room saved successfully.")
            return redirect('dashboard:admin_landing')
        else:
            messages.error(request, "Error saving room. Please check the form.")
    else:
        form = RoomForm(instance=room)

    return render(request, 'dashboard/add_or_modify_room.html', {
        'form': form,
        'room': room
    })

@login_required
def add_or_modify_category(request, category_id=None):
    category = get_object_or_404(RoomCategory, id=category_id) if category_id else None  # Updated Category to RoomCategory

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category saved successfully.")
            return redirect('dashboard:admin_landing')
        else:
            messages.error(request, "Error saving category. Please check the form.")
    else:
        form = CategoryForm(instance=category)

    return render(request, 'dashboard/add_or_modify_category.html', {
        'form': form,
        'category': category
    })

@login_required
def modify_room_landing(request):
    rooms = Room.objects.all()
    return render(request, 'dashboard/modify_room_landing.html', {'rooms': rooms})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully.")
            return redirect('dashboard:modify_category_landing')
        else:
            messages.error(request, "Error adding category. Please check the form.")
    else:
        form = CategoryForm()

    return render(request, 'dashboard/add_category.html', {'form': form})

@login_required
def modify_category(request, id):
    category = get_object_or_404(RoomCategory, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)  # Include request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('dashboard:modify_category_landing')
        else:
            messages.error(request, "Error updating category. Please check the form.")
    else:
        form = CategoryForm(instance=category)

    return render(request, 'dashboard/modify_category.html', {'form': form , 'category': category})

@login_required
def modify_category_landing(request):
    categories = RoomCategory.objects.all()  # Updated from Category to RoomCategory
    return render(request, 'dashboard/modify_category_landing.html', {'categories': categories})

def admin_logout(request):
    logout(request)
    return redirect('dashboard:login')
