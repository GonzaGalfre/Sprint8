from posixpath import basename
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'client_data', views.ClienteViewSet, basename='cd')
router.register(r'account_data', views.CuentaViewSet, basename='ad')



app_name = 'clientes'
urlpatterns = [
    path('resumen/', views.index, name='index'),
    path('prestamos/', views.prestamos, name='prestamos'),
    path('cotizaciones/', views.cotizaciones, name='cotizaciones'),
    path('api/', include(router.urls), name='api'),
]