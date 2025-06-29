# main/urls.py

from django.urls import path
from . import views

# This namespace is required for {% url 'main:...' %} to work.
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
    path('encuesta/', views.encuesta, name='encuesta'),
    path('politica/', views.politica, name='politica'),
    path('servicios/', views.servicios, name='servicios'),
    path('videos/', views.videos, name='videos'),
    
    # --- VERIFY THESE URLS ---
    # This maps the /repertorio/ URL to the repertorio_list view.
    # Its name 'repertorio_list' matches the template's link.
    path('repertorio/', views.repertorio_list, name='repertorio_list'),
    
    # This maps /repertorio/5/ (for example) to the repertorio_detail view.
    # It captures the number as an integer 'pk' and passes it to the view.
    # Its name 'repertorio_detail' matches the template's link.
    path('repertorio/<int:pk>/', views.repertorio_detail, name='repertorio_detail'),
    
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
]