from django import forms
from namaste_app.models import RequestAppointment, MessageRequest, Customer, CustomerEntry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RequestForm(forms.ModelForm): 
    class Meta:
        model = RequestAppointment
        fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'address', 'zip', 'city', 'service', 'date', 'time']

        service = forms.ChoiceField(choices=[('Masajes', 'Masajes'), ('Drenajes', 'Drenajes'), ('Tratamientos', 'Tratamientos'), ('Depilación', 'Depilación')])

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
    
