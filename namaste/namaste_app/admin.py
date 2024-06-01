from django.contrib import admin

# Register your models here.
from .models import RequestAppointment, MessageRequest

admin.site.register(RequestAppointment)
admin.site.register(MessageRequest)