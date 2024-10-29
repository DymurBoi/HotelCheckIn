from django.contrib import admin
from .models import Room,Reservation

# Register your models here.

admin.site.register(Room)
admin.site.register(Reservation)


'''
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'room_price', 'rooms_available') 
    search_fields = ('room_type',) 
    list_filter = ('room_type',) 

'''
