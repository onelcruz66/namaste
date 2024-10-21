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
    path('laser/', views.laser, name='laser'),
    path('vacumterapia/', views.vacumterapia, name='vacumterapia'),
    path('mesoterapia/', views.mesoterapia, name='mesoterapia'),
    path('post-parto/', views.post_parto, name='post_parto'),
    path('lebody/', views.lebody, name='lebody'),
    path('relevo/', views.relevo, name='relevo'),
    path('relevo-clientes/', views.relevo_clientes, name='relevo-clientes'),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('auth/logout/', views.logout, name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("mensajes/", views.mensajes, name="mensajes"),
    path("registro/", views.registro, name="registro"),
    path("informacion-de-cliente/", views.informacion_de_cliente, name="informacion_de_cliente"),
    path("informacion-de-cliente/<int:user_id>/", views.informacion_de_cliente, name="informacion_de_cliente"),
    path("buscar-cliente/", views.buscar_cliente, name="buscar_cliente"),
    path("borrar-cliente/<int:user_id>/", views.borrar_cliente, name="borrar_cliente"),
    path("borrar-entrada/<int:user_id>/", views.borrar_entrada, name="borrar_entrada"),
    path("borrar-mensaje/<int:user_id>/", views.borrar_mensajes, name="borrar_mensajes"),
    path("check-phone/", views.check_phone, name="check-phone"),
    path("check-email/", views.check_email, name="check-email"),
    path("booking/", views.booking, name="booking"),
    path("hora/", views.hora, name="hora"),
    path("hora/<int:appointment_id>/", views.hora, name="hora"),
    path("payment/", views.payment, name="payment"),
    path("payment-confirmation/", views.payment_confirmation, name="payment_confirmation"),
    path("payment-error/", views.payment_error, name="payment_error"),
    path('config/', views.stripe_config, name="config"),
    path('create-checkout-session/', views.create_checkout_session),
    path('webhook/', views.stripe_webhook),
    path("agenda/", views.agenda, name="agenda"),
    path("gracias/", views.gracias, name="gracias"),
    path("citas-solicitadas/", views.citas_solicitadas, name="citas-solicitadas"),
    path("borrar-cita/<int:user_id>/", views.borrar_cita, name="borrar_cita"),
]
