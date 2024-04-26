from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('service/', views.service, name='service'),
    path('swedish-massage/', views.swedish_massage, name='swedish-massage'),
]
