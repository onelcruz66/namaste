from django.shortcuts import render, redirect
from django.http import HttpResponse
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


label_to_field = {
    '9:00': 'nine',
    '10:00': 'ten',
    '11:00': 'eleven',
    '12:00': 'twelve',
    '1:00': 'one',
    '2:00': 'two',
    '3:00': 'three',
    '4:00': 'four',
    '5:00': 'five'
}

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

@login_required
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
            return redirect('buscar_cliente')  # Redirect after POST
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

        if request.method == 'POST':
            response = handlePostRequestForNewTimeSlot(request, lastAppointment)
            if response:
                return response

    return render(request, "time.html", context)

def handlePostRequestForNewTimeSlot(request, lastAppointment):
    new_time_slot_record = TimeSlots(
        date = lastAppointment.date,
        hour_selected = request.POST.get('hour_selected')
    )
    new_time_slot_record.save()
    time_slot = new_time_slot_record.hour_selected
    subtractTimeSlotFromDb(new_time_slot_record, time_slot)
    form = TimeForm(request.POST)
    if form.is_valid():
        return redirect('home')
    else:
        print(form.errors)
        print("time_slot:", time_slot)
    return None

def handlePostRequestForExistingTimeSlot(request, timeSlotObject):

    form = TimeForm(request.POST)
    if form.is_valid():
        time_slot = request.POST.get('hour_selected')
        subtractTimeSlotFromDb(timeSlotObject, time_slot)
        
        return redirect('home')
    else:
        print(form.errors)
        print("time_slot:", time_slot)
    return None

def subtractTimeSlotFromDb(dbObject, time_slot):
    if time_slot == '9:00' and dbObject.nine != 0:
        dbObject.nine = dbObject.nine - 1
        dbObject.save()
        return
    elif time_slot == '10:00' and dbObject.ten != 0:
        dbObject.ten = dbObject.ten - 1
        dbObject.save()
        return
    elif time_slot == '11:00' and dbObject.eleven != 0:
        dbObject.eleven = dbObject.eleven - 1
        dbObject.save()
        return
    elif time_slot == '12:00' and dbObject.twelve != 0:
        dbObject.twelve = dbObject.twelve - 1
        dbObject.save()
        return
    elif time_slot == '1:00' and dbObject.one != 0:
        dbObject.one = dbObject.one - 1
        dbObject.save()
        return
    elif time_slot == '2:00' and dbObject.two != 0:
        dbObject.two = dbObject.two - 1
        dbObject.save()
        return
    elif time_slot == '3:00' and dbObject.three != 0:
        dbObject.three = dbObject.three - 1
        dbObject.save()
        return
    elif time_slot == '4:00' and dbObject.four != 0:
        dbObject.four = dbObject.four - 1
        dbObject.save()
        return
    elif time_slot == '5:00' and dbObject.five != 0:
        dbObject.five = dbObject.five - 1
        dbObject.save()
        return
    else:
        return



    