from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

def services(request):
    return render(request, 'services.html')

def service(request):
    return render(request, 'service-single.html')

def swedish_massage(request):
    return render(request, 'swedish_massage.html')