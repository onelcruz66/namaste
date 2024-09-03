from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import RequestAppointment, MessageRequest, ApprovedAppointments, Customer, CustomerEntry, TimeSlots
from namaste_app.forms import RequestForm, MessageForm, CreateUserForm, CustomAuthenticationForm, SignatureForm, TimeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
import base64
from django.core.files.base import ContentFile
from django import forms
import json
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from namaste.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_WEBHOOK_SECRET
import stripe
from django.views.decorators.csrf import csrf_exempt

from .utilities import *

stripe.api_key = STRIPE_SECRET_KEY

# Create your views here.
def home(request):
    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, "index.html", context)

def sobre_nosotros(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'about-us.html', context)

def contacto(request):

    context = {}

    if request.method == "POST":
        if 'contact_form' in request.POST:
            contact_form = MessageForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect(request.path)
        elif 'request_form' in request.POST:
            request_form = RequestForm(request.POST)
            if request_form.is_valid():
                request_form.save()
                return redirect(request.path)
    else:
        contact_form = MessageForm()
        request_form = RequestForm()

    context['contact_form'] = contact_form
    context['request_form'] = request_form

    return render(request, 'contact-us.html', context)

def servicios(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'services.html', context)

def masaje_sueco(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'swedish_massage.html', context)

def post_operatorio(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'post_op.html', context)

def masaje_prenatal(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'prenatal.html', context)

def masaje_profundo(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'deep_massage.html', context)

def detox_oro(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'gold_detox.html', context)

def vacuslim(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'vacuslim.html', context)

def waxing(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'waxing.html', context)

def terapia_madera(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'wood_therapy.html', context)

def terapia_metal(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'metal_therapy.html', context)

def drenaje(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'drainage.html', context)

def quiromasaje(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'massage_therapy.html', context)

def copas_chinas(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'chinese_cups.html', context)

def pistola_masaje(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'massage_pistol.html', context)

def maderoterapia_facial(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'facial_wood_therapy.html', context)

def lipolaser(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'lipolaser.html', context)

def vacumterapia(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'vacumterapia.html', context)

def lebody(request):

    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path) 
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, 'lebody.html', context)

def relevo(request):

    context = {}

    if request.method == 'POST':
        form = SignatureForm(request.POST)
        if form.is_valid():
            has_condition = form.cleaned_data['has_condition']
            condition_names = form.cleaned_data['condition_names']
            if has_condition and not condition_names:
                form.add_error('condition_names', 'Please enter at least one condition name.')

            # Create a new document instance but do not save it yet
            new_doc = Customer(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                address=form.cleaned_data['address'],
                has_condition=has_condition,
                condition_names=condition_names,
                accept_photo=form.cleaned_data['accept_photo'],
                accept_publishing=form.cleaned_data['accept_publishing']
            )
            signature_data = request.POST.get('signature')
            if signature_data:
                format, imgstr = signature_data.split(';base64,')  # format ~= data:image/png;base64
                ext = format.split('/')[-1]  # assume image/png
                data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

                new_doc.signature.save(f"{new_doc.first_name}_signature.{ext}", data, save=False)

            new_doc.save()
            return redirect('home')  # Redirect after POST
    else:
        form = SignatureForm()

    context['form'] = form

    return render(request, 'relevo.html', context)

# Admin page views.
@login_required
def dashboard(request):
    context = {}
    request_appointment_table = RequestAppointment.objects.all()
    message_request_table = MessageRequest.objects.all()
    approved_appointment_table = ApprovedAppointments.objects.all()
    signed_document_table = Customer.objects.all()
    context['request_appointment_table'] = request_appointment_table
    context['message_request_table'] = message_request_table
    context['approved_appointment_table'] = approved_appointment_table
    context['signed_document_table'] = signed_document_table

    return render(request, "dashboard.html", context)

@login_required
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'register.html', context)

def logout(request):
    return redirect('login')

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

@login_required
def mensajes(request):
    context = {}
    message = MessageRequest.objects.order_by('id')
    context['message'] = message

    return render(request, "mensajes.html", context)

@login_required
def registro(request):
    context = {}
    try:
        customer_entries = CustomerEntry.objects.order_by('-date_seen')
        context['customer_entries'] = customer_entries
    except Exception as e:
        return f"Error fetching records: {str(e)}"

    return render(request, "registro.html", context)

@login_required
def informacion_de_cliente(request, user_id):
    context = {}

    user = Customer.objects.get(id=user_id)

    if request.method == 'POST':
        treatment = request.POST.get('treatment')
        payment_type = request.POST.get('payment_type')
        payment_amount = request.POST.get('payment_amount')
        comments = request.POST.get('comments')

        new_doc = CustomerEntry(
                customer=user,
                treatment=treatment,
                payment_type=payment_type,
                payment_amount=payment_amount,
                comments=comments,
            )
        
        new_doc.save()
        return redirect('registro')

    else:
        context['user'] = user
        return render(request, 'informacion_de_cliente.html', context)


@login_required
def buscar_cliente(request):
    context = {}

    try:
        # customer_entries = CustomerEntry.objects.all()
        customer = Customer.objects.order_by('id')
        context['customer'] = customer
    except Exception as e:
        return f"Error fetching records: {str(e)}"

    # GET request returns the empty search form
    return render(request, "buscar_cliente.html", context)


@login_required
def borrar_entrada(request, user_id):
    entry = CustomerEntry.objects.get(pk=user_id)
    entry.delete()
    return redirect('registro')

@login_required
def borrar_cliente(request, user_id):
    customer_user = Customer.objects.get(pk=user_id)
    customer_user.delete()
    return redirect('buscar_cliente')

@login_required
def borrar_mensajes(request, user_id):
    mensaje = MessageRequest.objects.get(pk=user_id)
    mensaje.delete()
    return redirect('mensajes')

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'exists': Customer.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)

def check_phone(request):
    phone_number = request.GET.get('phone_number', None)
    data = {
        'exists': Customer.objects.filter(phone_number=phone_number).exists()
    }
    return JsonResponse(data)

def booking(request):
    context = {}

    # Handle form submissions
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()

            # After database entry is saved, pass in the db object id to the hora view.
            getRequestedAppointment = RequestAppointment.objects.last()
            return redirect('hora', appointment_id=getRequestedAppointment.id) 
        else:
            print(form.errors)
    else:
        # Render the form for GET requests
        form = RequestForm()

    context['form'] = form

    return render(request, "booking.html", context)


def hora(request, appointment_id):
    context = {}
    lastAppointment = RequestAppointment.objects.get(pk=appointment_id)
    context['last_appointment'] = lastAppointment

    try:

        timeSlot = TimeSlots.objects.get(date=lastAppointment.date)
        context['time_slots'] = timeSlot

        if request.method == 'POST':
            response = handlePostRequestForExistingTimeSlot(request, timeSlot)
            if response:
                return response

    except TimeSlots.DoesNotExist:

        form = TimeForm()
        context['time_slots'] = form
        context['nine'] = 3
        context['ten'] = 3
        context['eleven'] = 3
        context['twelve'] = 3
        context['one'] = 3
        context['two'] = 3
        context['three'] = 3
        context['four'] = 3
        context['five'] = 3

        if request.method == 'POST':
            response = handlePostRequestForNewTimeSlot(request, lastAppointment)
            if response:
                return response

    return render(request, "time.html", context)


def payment(request):
    context = {}
    context['stripe_public_key'] = STRIPE_PUBLIC_KEY
    
    return render(request, 'payments.html', context)

def payment_confirmation(request):
    context = {}

    return render(request, 'confirm_payment.html', context)

def payment_error(request):
    context = {}

    return render(request, 'error_payment.html', context)

@csrf_exempt
def stripe_config(request):
    
    stripe_config = {'publicKey': STRIPE_PUBLIC_KEY}
    return JsonResponse(stripe_config, safe=False)
    

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'payment-confirmation?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'payment-error/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 1500,
                        'product_data': {
                            'name': 'Deposito Regular',
                        },
                    },
                    'quantity': 1,
                },
            ],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = STRIPE_SECRET_KEY
    endpoint_secret = STRIPE_WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)

@login_required
def agenda(request):
    context = {}

    return render(request, "agenda.html", context)