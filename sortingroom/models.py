from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from dashboard.models import Room

# Create your models here.

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()
    special_request = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Check if check-out is after check-in
        if self.check_out <= self.check_in:
            raise ValidationError("Check-out date must be after check-in date.")

        # Optional: Ensure check-in is not in the past
        if self.check_in < date.today():
            raise ValidationError("Check-in date cannot be in the past.")

    def __str__(self):
        return f'Reservation for {self.first_name} {self.last_name} - {self.room.room_category.category_id} Room {self.room.room_id}'
    

class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    payment_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=20, null=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=20, default="Pending")


    def __str__(self):
        return f'Room ID:{self.reservation.room.room_id} {self.reservation.room.room_category.category_id}- {self.payment_total} - {self.payment_method} - {self.payment_status} (Payment ID: {self.id})'


