from django.contrib import admin

from .models import Room, Message, PhoneNumber  , IpAddr

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(PhoneNumber)
admin.site.register(IpAddr)