from django.db import models

class RoomCategory(models.Model):
    category_id = models.CharField(max_length=100,default="Standard")
    room_photo = models.ImageField( blank=True, null=True,default= "lizard.jpeg")
    room_desc = models.TextField(max_length=200, blank=True)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
 
    def __str__(self):
        return f"{self.category_id} - ${self.room_price}"
 
class Room(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    room_id = models.CharField(max_length=50,default=" ")
    is_available = models.BooleanField(default=True)
 
    def __str__(self):
        return f"{self.room_id} - ({self.room_category}) - Available: {self.is_available}"
