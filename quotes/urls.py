from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('cotizador/', views.cotizador_view, name='cotizador'),
    path('cotizacion-recibida/<str:code>/', views.ver_cotizacion_view, name='ver_cotizacion'),
    # Restore the link to the correct, fully-featured view.
    path('cotizacion/<str:code>/', views.cotizacion_detail_view, name='cotizacion_detail'),
    path('rastrear-cotizacion/', views.rastrear_cotizacion_view, name='rastrear_cotizacion'),
]