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
    return render(request, 'about-us.html')

def contacto(request):
    return render(request, 'contact-us.html')

def servicios(request):
    return render(request, 'services.html')

def servicio(request):
    return render(request, 'service-single.html')

def masaje_sueco(request):
    return render(request, 'swedish_massage.html')

def post_operatorio(request):
    return render(request, 'post_op.html')

def masaje_prenatal(request):
    return render(request, 'prenatal.html')

def masaje_profundo(request):
    return render(request, 'deep_massage.html')

def detox_oro(request):
    return render(request, 'gold_detox.html')

def vacuslim(request):
    return render(request, 'vacuslim.html')

def waxing(request):
    return render(request, 'waxing.html')

def terapia_madera(request):
    return render(request, 'wood_therapy.html')

def terapia_metal(request):
    return render(request, 'metal_therapy.html')

def drenaje(request):
    return render(request, 'drainage.html')

def quiromasaje(request):
    return render(request, 'massage_therapy.html')

def copas_chinas(request):
    return render(request, 'chinese_cups.html')

def pistola_masaje(request):
    return render(request, 'massage_pistol.html')

def maderoterapia_facial(request):
    return render(request, 'facial_wood_therapy.html')

def lipolaser(request):
    return render(request, 'lipolaser.html')

def vacumterapia(request):
    return render(request, 'vacumterapia.html')

def lebody(request):
    return render(request, 'lebody.html')