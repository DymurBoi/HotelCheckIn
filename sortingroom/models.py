from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from accounts.models import CustomUser
# Create your models here.

class Room(models.Model):
    room_photo = models.ImageField(default = 'fallback.png', blank=True)
    room_type = models.CharField(max_length=30)
    room_desc = models.TextField(max_length=200, blank=True)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_available = models.IntegerField(default=0)
    room_check_in = models.BooleanField(default=False,null=True)
    def __str__(self):
        return f"{self.room_type} - ${self.room_price}"
    

class Reservation(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()
    special_request = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustomUser, null=True ,  on_delete=models.SET_NULL)
    def clean(self):
        # Check if check-out is after check-in
        if self.check_out <= self.check_in:
            raise ValidationError("Check-out date must be after check-in date.")

        # Optional: Ensure check-in is not in the past
        if self.check_in < date.today():
            raise ValidationError("Check-in date cannot be in the past.")

    def __str__(self):
        return f'Reservation for {self.first_name} {self.last_name} - {self.room.room_type}'
    

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    payment_total = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    payment_method = models.CharField(max_length=20, null=True)
    payment_status = models.CharField(max_length=20, default="Pending")


