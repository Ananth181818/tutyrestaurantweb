from django.db import models

class RoomBooking(models.Model):
    guest_name = models.CharField(max_length=100)
    guest_phone = models.CharField(max_length=20)
    room_type = models.CharField(max_length=100)
    price = models.CharField(max_length=20, default="0")
    check_in = models.DateField()
    check_out = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.room_type} ({self.check_in})"

