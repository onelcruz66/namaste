from django import forms
from namaste_app.models import RequestAppointment, MessageRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

class CustomAuthenticationForm(AuthenticationForm):
    # Add any additional fields or customization if needed
    pass