from django.contrib import admin
from .models import RoomBooking

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'room_type', 'price', 'check_in', 'check_out', 'booked_at')
    list_filter = ('room_type', 'check_in')
    search_fields = ('guest_name', 'guest_phone')

