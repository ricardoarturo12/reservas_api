from django.contrib import admin
from .models import Person, Client, Room, Reservation
# Register your models here.
admin.site.register(Person)
admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Reservation)