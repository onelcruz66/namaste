from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RequestAppointment, MessageRequest, ApprovedAppointments
from namaste_app.forms import RequestForm, MessageForm, CreateUserForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


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