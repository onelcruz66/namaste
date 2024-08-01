from django.contrib import admin

# Register your models here.
from .models import RequestAppointment, MessageRequest, Customer, CustomerEntry, TimeSlots

admin.site.register(RequestAppointment)
admin.site.register(MessageRequest)
admin.site.register(Customer)
admin.site.register(CustomerEntry)
admin.site.register(TimeSlots)