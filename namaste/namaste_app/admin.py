from django.contrib import admin

# Register your models here.
from .models import RequestAppointment, MessageRequest, Customer, CustomerEntry

admin.site.register(RequestAppointment)
admin.site.register(MessageRequest)
admin.site.register(Customer)
admin.site.register(CustomerEntry)