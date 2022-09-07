from django.urls import path, include
from . import views

app_name = 'clientes'
urlpatterns = [
    path('resumen/', views.index, name='index'),
    path('prestamos/', views.prestamos, name='prestamos'),
    path('cotizaciones/', views.cotizaciones, name='cotizaciones'),
]