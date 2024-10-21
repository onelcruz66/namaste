from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import json
import uuid


# Create your models here.
class ServiceType(models.TextChoices):
    GOLDDETOXPACKAGE = 'Gold Detox (6 Secciones)', _('Gold Detox (6 Secciones)')
    METALOTERAPIAPACKAGE = 'Metaloterapia (6 Secciones)', _('Metaloterapia (6 Secciones)')
    MADEROTERAPIAPACKAGE = 'Maderoterapia (6 Secciones)', _('Maderoterapia (6 Secciones)')
    MASAJESUECO = 'Masaje Sueco', _('Masaje Sueco')
    POSTOPERATORIO = 'Post-Operatorio', _('Post-Operatorio')
    MASAJEPRENATAL = 'Masaje Prenatal', _('Masaje Prenatal')
    MASAJEPROFUNDO = 'Masaje Profundo', _('Masaje Profundo')
    GOLDDETOX = 'Gold Detox', _('Gold Detox')
    VACUSLIM = 'Vacuslim-48', _('Vacuslim-48')
    DEPILACION = 'Depilación', _('Depilación')
    MADEROTERAPIA = 'Maderoterapia', _('Maderoterapia')
    METALOTERAPIA = 'Metaloterapia', _('Metaloterapia')
    DRENAJELINFATICO = 'Drenaje Linfático', _('Drenaje Linfático')
    QUIROMASAJE = 'Quiromasaje', _('Quiromasaje')
    COPASCHINAS = 'Copas Chinas', _('Copas Chinas')
    PISTOLAMASAJE = 'Pistola De Masaje', _('Pistola De Masaje')
    MADEROTERAPIAFACIAL = 'Maderoterapia Facial', _('Maderoterapia Facial')
    LIPOLASER = 'Lipoláser', _('Lipoláser')
    VACUMTERAPIA = 'Vacumterapia', _('Vacumterapia')
    LEBODY = 'LeBody', _('LeBody')
    POSTPARTO = 'Post Parto', _('Post Parto')
    MESOTERAPIA = 'Mesoterapia', _('Mesoterapia')
    LASER = 'Laser', _('Laser')

class RequestAppointment(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False, default='')
    email_address = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=50, blank=True, default='')
    zip = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    service = models.CharField(max_length=50, choices=ServiceType.choices, default='')
    date_requested = models.CharField(max_length=50, blank=False, default='')


class HourSelected(models.TextChoices):
    NINE = '9:00', _('9:00')
    TEN = '10:00', _('10:00')
    ELEVEN = '11:00', _('11:00')
    TWELVE = '12:00', _('12:00')
    ONE = '1:00', _('1:00')
    TWO = '2:00', _('2:00')
    THREE = '3:00', _('3:00')
    FOUR = '4:00', _('4:00')
    FIVE = '5:00', _('5:00')

class TimeSlots(models.Model):
    date = models.CharField(max_length=50, blank=False, default='')
    MY_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )
    hour_selected = models.CharField(max_length=50, choices=HourSelected.choices, default='')
    nine = models.IntegerField(choices=MY_CHOICES, default=3)
    ten = models.IntegerField(choices=MY_CHOICES, default=3)
    eleven = models.IntegerField(choices=MY_CHOICES, default=3)
    twelve = models.IntegerField(choices=MY_CHOICES, default=3)
    one = models.IntegerField(choices=MY_CHOICES, default=3)
    two = models.IntegerField(choices=MY_CHOICES, default=3)
    three = models.IntegerField(choices=MY_CHOICES, default=3)
    four = models.IntegerField(choices=MY_CHOICES, default=3)
    five = models.IntegerField(choices=MY_CHOICES, default=3)

    def save(self, *args, **kwargs):
        if not self.id:
            self.nine = 3
            self.ten = 3
            self.eleven = 3
            self.twelve = 3
            self.one = 3
            self.two = 3
            self.three = 3
            self.four = 3
            self.five = 3
        super(TimeSlots, self).save(*args, **kwargs)

class MessageRequest(models.Model):
    first_name = models.CharField(max_length=80, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False, default='')
    email_address = models.CharField(max_length=50, blank=False, default='')
    question = models.TextField(max_length=200, null=False, blank=False)

class ApprovedServiceType(models.TextChoices):
    MASAJES = 'Masajes', _('Masajes')
    DRENAJES = 'Drenajes', _('Drenajes')
    TRATAMIENTOS = 'Tratamientos', _('Tratamientos')
    DEPILACION = 'Depilación', _('Depilación')

class ApprovedAppointments(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False, default='')
    email_address = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=50, blank=True, default='')
    zip = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    service = models.CharField(max_length=50, choices=ApprovedServiceType.choices, default='')
    date = models.CharField(max_length=50, blank=False, default='')
    time = models.CharField(max_length=50, blank=False, default='')


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, default='')
    last_name = models.CharField(max_length=50, null=False, blank=False, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=True, default='')
    has_condition = models.BooleanField(default=False, verbose_name="Has Condition")
    condition_names = models.CharField(max_length=100, null=True, blank=True, verbose_name="Condition Names")
    accept_photo = models.BooleanField(default=False, verbose_name="Accepts Pictures")
    accept_publishing = models.BooleanField(default=False, verbose_name="Accepts Publishing")
    sign_date = models.DateTimeField(null=True, blank=True)
    signature = models.ImageField(upload_to='signatures/', null=True, blank=True, default='')  # Stores the path to the signature image

    def save(self, *args, **kwargs):
        # Set the sign_date to now only if it's None (i.e., new instance)
        if not self.sign_date:
            self.sign_date = timezone.now()
        super().save(*args, **kwargs)

class PaymentType(models.TextChoices):
    ATHMOVIL = 'ATHMovil', _('ATHMovil')
    CASH = 'Cash', _('Cash')
    CREDIT = 'Credit', _('Credit')
    DEBIT = 'Debit', _('Debit')

class TreatmentType(models.TextChoices):
    MASAJESUECO = 'Masaje Sueco', _('Masaje Sueco')
    POSTOPERATORIO = 'Post Operatorio', _('Post Operatorio')
    MASAJEPRENATAL = 'Masaje Prenatal', _('Masaje Prenatal')
    MASAJEPROFUNDO = 'Masaje Profundo', _('Masaje Profundo')
    GOLDDETOX = 'Gold Detox', _('Gold Detox')
    VACUSLIM = 'Vacuslim-48', _('Vacuslim-48')
    DEPILACION = 'Depilacion', _('Depilacion')
    MADEROTERAPIA = 'Maderoterapia', _('Maderoterapia')
    METALOTERAPIA = 'Metaloterapia', _('Metaloterapia')
    DRENAJELINFATICO = 'Drenaje Linfatico', _('Drenaje Linfatico')
    QUIROMASAJE = 'Quiromasaje', _('Quiromasaje')
    COPASCHINAS = 'Copas Chinas', _('Copas Chinas')
    PISTOLAMASAJE = 'Pistola de Masaje', _('Pistola de Masaje')
    MADEROTERAPIAFACIAL = 'Maderoterapia Facial', _('Maderoterapia Facial')
    LIPOLASER = 'Lipolaser', _('Lipolaser')
    VACUMTERAPIA = 'Vacumterapia', _('Vacumterapia')
    LEBODY = 'LeBody', _('LeBody')
    MESOTERAPIA = 'Mesoterapia', _('Mesoterapia')
    POSTPARTO = 'Post Parto', _('Post Parto')
    LASER = 'Laser', _('Laser')
    OTRO = 'Otro', _('Otro')

class CustomerEntry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='entries')
    date_seen = models.DateTimeField(auto_now_add=True, verbose_name="Date Seen")
    treatment = models.CharField(max_length=50, choices=TreatmentType.choices, default='')
    payment_type = models.CharField(max_length=50, choices=PaymentType.choices, default='')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in dollars")
    comments = models.CharField(max_length=300, blank=True, default='')

    # Converts dollar amounts to cents if needed for calculations or integration with systems that require cents.
    def get_price_in_cents(self):
        return int(self.price * 100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name