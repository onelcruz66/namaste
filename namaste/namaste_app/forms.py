from django import forms
from namaste_app.models import RequestAppointment, MessageRequest, Customer, CustomerEntry, TimeSlots
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RequestForm(forms.ModelForm): 
    class Meta:
        model = RequestAppointment
        fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'address', 'zip', 'city', 'service', 'date']

        service = forms.ChoiceField(choices=[('Gold Detox (6 Secciones)', 'Gold Detox (6 Secciones)'), \
                                             ('Metaloterapia (6 Secciones)', 'Metaloterapia (6 Secciones)'), \
                                             ('Maderoterapia (6 Secciones)', 'Maderoterapia (6 Secciones)'), \
                                             ('Masaje Sueco', 'Masaje Sueco'), \
                                             ('Post-Operatorio', 'Post-Operatorio'), \
                                             ('Masaje Prenatal', 'Masaje Prenatal'), \
                                             ('Masaje Profundo', 'Masaje Profundo'), \
                                             ('Gold Detox', 'Gold Detox'), \
                                             ('Vacuslim-48', 'Vacuslim-48'), \
                                             ('Depilación', 'Depilación'), \
                                             ('Maderoterapia', 'Maderoterapia'), \
                                             ('Metaloterapia', 'Metaloterapia'), \
                                             ('Depilación', 'Depilación'), \
                                             ('Drenaje Linfático', 'Drenaje Linfático'), \
                                             ('Quiromasaje', 'Quiromasaje'), \
                                             ('Copas Chinas', 'Copas Chinas'), \
                                             ('Pistola De Masaje', 'Pistola De Masaje'), \
                                             ('Maderoterapia Facial', 'Maderoterapia Facial'), \
                                             ('Lipoláser', 'Lipoláser'), \
                                             ('Vacumterapia', 'Vacumterapia'), \
                                             ('LeBody', 'LeBody')
                                             ])

class TimeForm(forms.ModelForm):

    class Meta:
        model = TimeSlots
        fields = ['hour_selected']

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageRequest
        fields = ['first_name', 'last_name', 'email_address', 'question']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        # Remove help texts
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class CustomAuthenticationForm(AuthenticationForm):
    # Add any additional fields or customization if needed
    pass

class SignatureForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'has_condition', 'condition_names', 'accept_photo', 'accept_publishing', 'sign_date', 'signature']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Customer.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This phone number is already in use.")
        return phone_number

class ClientForm(forms.ModelForm):

    class Meta:
        model = CustomerEntry
        fields = ['treatment', 'payment_type', 'payment_amount', 'comments']

        payment_type = forms.ChoiceField(choices=[('ATHMovil', 'ATHMovil'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('Debit', 'Debit')])

        treatment = forms.ChoiceField(choices=[('Masaje Sueco', 'Masaje Sueco'), \
                                               ('Post Operatorio', 'Post Operatorio'), \
                                               ('Masaje Prenatal', 'Masaje Prenatal'), \
                                               ('Masaje Profundo', 'Masaje Profundo'), \
                                               ('Gold Detox', 'Gold Detox'), \
                                               ('Vacuslim-48', 'Vacuslim-48'), \
                                               ('Depilacion', 'Depilacion'), \
                                               ('Maderoterapia', 'Maderoterapia'), \
                                               ('Metaloterapia', 'Metaloterapia'), \
                                               ('Drenaje Linfatico', 'Drenaje Linfatico'), \
                                               ('Quiromasaje', 'Quiromasaje'), \
                                               ('Copas Chinas', 'Copas Chinas'), \
                                               ('Pistola de Masaje', 'Pistola de Masaje'), \
                                               ('Maderoterapia Facial', 'Maderoterapia Facial'), \
                                               ('Lipolaser', 'Lipolaser'), \
                                               ('Vacumterapia', 'Vacumterapia'), \
                                               ('LeBody', 'LeBody'), \
                                               ('Otro', 'Otro'), \
                                               ])