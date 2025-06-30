# quotes/urls.py

from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('cotizador/', views.cotizador_view, name='cotizador'),
    # This is the initial "Thank You" preview page
    path('cotizacion-recibida/<str:code>/', views.ver_cotizacion_view, name='ver_cotizacion'),
    # This is the full, trackable detail page with program and payment info
    #path('cotizacion/<str:code>/', views.cotizacion_detail_view, name='cotizacion_detail')
    path('cotizacion/<str:code>/', views.ver_cotizacion_view, name='ver_cotizacion_view'),
    path('rastrear-cotizacion/', views.rastrear_cotizacion_view, name='rastrear_cotizacion'),
]