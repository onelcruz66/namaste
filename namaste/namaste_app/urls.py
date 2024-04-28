from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre-nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('servicio/', views.servicio, name='servicio'),
    path('masaje-sueco/', views.masaje_sueco, name='masaje-sueco'),
    path('post-operatorio/', views.post_operatorio, name='post-operatorio'),
    path('masaje-prenatal/', views.masaje_prenatal, name='masaje-prenatal'),
    path('masaje-profundo/', views.masaje_profundo, name='masaje-profundo'),
    path('detox-oro/', views.detox_oro, name='detox-oro'),
    path('vacuslim/', views.vacuslim, name='vacuslim'),
    path('waxing/', views.waxing, name='waxing'),
    path('terapia-madera/', views.terapia_madera, name='terapia-madera'),
    path('terapia-metal/', views.terapia_metal, name='terapia-metal'),
    path('drenaje/', views.drenaje, name='drenaje'),
    path('quiromasaje/', views.quiromasaje, name='quiromasaje'),
    path('terapia-bamboo/', views.terapia_bamboo, name='terapia-bamboo'),
    path('piedras-calientes/', views.piedras_calientes, name='piedras-calientes'),
    path('copas-chinas/', views.copas_chinas, name='copas-chinas'),
    path('pistola-masaje/', views.pistola_masaje, name='pistola-masaje'),
    path('mesoterapia/', views.mesoterapia, name='mesoterapia'),
]
