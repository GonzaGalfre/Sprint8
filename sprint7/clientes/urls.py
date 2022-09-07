from posixpath import basename
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'client_data', views.ClienteViewSet, basename='cd')
router.register(r'account_data', views.CuentaViewSet, basename='ad')
router.register(r'client_loans', views.PrestamoViewSet, basename='cl')
router.register(r'loans_by_branch/(?P<id>\d+)', views.SucursalViewSet, basename='br')



app_name = 'clientes'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('resumen/', views.index, name='index'),
    path('prestamos/', views.prestamos, name='prestamos'),
    path('cotizaciones/', views.cotizaciones, name='cotizaciones'),
    path('api/', include(router.urls), name='api'),
]