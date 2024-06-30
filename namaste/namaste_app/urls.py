from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre-nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('masaje-sueco/', views.masaje_sueco, name='masaje-sueco'),
    path('post-operatorio/', views.post_operatorio, name='post-operatorio'),
    path('masaje-prenatal/', views.masaje_prenatal, name='masaje-prenatal'),
    path('masaje-profundo/', views.masaje_profundo, name='masaje-profundo'),
    path('gold-detox/', views.detox_oro, name='detox-oro'),
    path('vacuslim/', views.vacuslim, name='vacuslim'),
    path('depilacion/', views.waxing, name='waxing'),
    path('terapia-madera/', views.terapia_madera, name='terapia-madera'),
    path('terapia-metal/', views.terapia_metal, name='terapia-metal'),
    path('drenaje/', views.drenaje, name='drenaje'),
    path('quiromasaje/', views.quiromasaje, name='quiromasaje'),
    path('copas-chinas/', views.copas_chinas, name='copas-chinas'),
    path('pistola-masaje/', views.pistola_masaje, name='pistola-masaje'),
    path('maderoterapia-facial/', views.maderoterapia_facial, name='maderoterapia-facial'),
    path('lipolaser/', views.lipolaser, name='lipolaser'),
    path('vacumterapia/', views.vacumterapia, name='vacumterapia'),
    path('lebody/', views.lebody, name='lebody'),
    path('relevo/', views.waiver, name='waiver'),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('auth/logout/', views.logout, name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("mensajes/", views.mensajes, name="mensajes"),
    path("registro/", views.registro, name="registro"),
    path("informacion-de-cliente/", views.informacion_de_cliente, name="informacion_de_cliente"),
    path("informacion-de-cliente/<int:user_id>/", views.informacion_de_cliente, name="informacion_de_cliente"),
    path("buscar-cliente/", views.buscar_cliente, name="buscar_cliente")
]
