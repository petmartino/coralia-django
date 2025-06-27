from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
    path('encuesta/', views.encuesta, name='encuesta'),
    path('politica/', views.politica, name='politica'),
    path('servicios/', views.servicios, name='servicios'),
    path('videos/', views.videos, name='videos'),
    path('repertorio/', views.repertorio_list, name='repertorio_list'),
    path('repertorio/<int:pk>/', views.repertorio_detail, name='repertorio_detail'),
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
]