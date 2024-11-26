from django.db import models

class RoomCategory(models.Model):
    category_id = models.CharField(max_length=30)
    room_photo = models.ImageField(default='fallback.png', blank=True)
    room_desc = models.TextField(max_length=200, blank=True)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def rooms_available(self):
        return Room.objects.filter(room_category=self, is_available=True).count()

    def __str__(self):
        return f"{self.id} {self.category_id} - {self.category_id} - P{self.room_price}"

class Room(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    room_id = models.CharField(max_length=10)
    room_photo = models.ImageField(default = 'fallback.png', blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_id} - ({self.room_category.category_id}) - Available: {self.is_available}"
