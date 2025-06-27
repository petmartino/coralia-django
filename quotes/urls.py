from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('cotizador/', views.cotizador_view, name='cotizador'),
    path('cotizacion/<str:code>/', views.ver_cotizacion_view, name='ver_cotizacion'),
    path('rastrear-cotizacion/', views.rastrear_cotizacion_view, name='rastrear_cotizacion'),
]