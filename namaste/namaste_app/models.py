from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ServiceType(models.TextChoices):
    MASAJES = 'Masajes', _('Masajes')
    DRENAJES = 'Drenajes', _('Drenajes')
    TRATAMIENTOS = 'Tratamientos', _('Tratamientos')
    DEPILACION = 'Depilación', _('Depilación')

class RequestAppointment(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=50, blank=False, default='')
    zip = models.CharField(max_length=50, blank=False, default='')
    city = models.CharField(max_length=50, blank=False, default='')
    service = models.CharField(max_length=50, choices=ServiceType.choices, default='')
    date = models.CharField(max_length=50, blank=False, default='')
    time = models.CharField(max_length=50, blank=False, default='')


class MessageRequest(models.Model):
    first_name = models.CharField(max_length=80, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    email_address = models.CharField(max_length=50, blank=False, default='')
    question = models.TextField(max_length=200, null=False, blank=False)

class ApprovedServiceType(models.TextChoices):
    MASAJES = 'Masajes', _('Masajes')
    DRENAJES = 'Drenajes', _('Drenajes')
    TRATAMIENTOS = 'Tratamientos', _('Tratamientos')
    DEPILACION = 'Depilación', _('Depilación')

class ApprovedAppointments(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=50, blank=False, default='')
    zip = models.CharField(max_length=50, blank=False, default='')
    city = models.CharField(max_length=50, blank=False, default='')
    service = models.CharField(max_length=50, choices=ApprovedServiceType.choices, default='')
    date = models.CharField(max_length=50, blank=False, default='')
    time = models.CharField(max_length=50, blank=False, default='')


    