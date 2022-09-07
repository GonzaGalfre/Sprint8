from django.shortcuts import render
from .models import Cliente
from cuentas.models import Cuenta, Movimientos
from tarjetas.models import Tarjeta, CardBrand
from .serializers import ClienteSerializer, CuentaSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


# Create your views here.

@login_required(login_url='/login/login/')
def index(request):

    
    clientdata = Cliente.objects.get(user_id = request.user.id)
    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
        accdatalen = len(Cuenta.objects.filter(customer_id = clientdata.customer_id))
    except:
        accdata = None

    try:
        cardsdata = Tarjeta.objects.filter(customer_id = clientdata.customer_id)
    except:
        cardsdata = None

    try:
        cbdata = CardBrand.objects.filter(card_brand_id = cardsdata.card_brand_id)
    except:
        cbdata = None

    if accdatalen <= 1:
        try:
            transactionsdata = [Movimientos.objects.filter(account_id = accdata[0].account_id)]
        except:
            transactionsdata = None
    else:
        transactionsdata = []
        for a in accdata:
            i = Movimientos.objects.filter(account_id = a.account_id)
            transactionsdata.append(i)


    context = {'clientdata':clientdata, 'accdata':accdata, 'cardsdata':cardsdata, 'cbdata':cbdata}
    return render(request, 'clientes/index.html', context)

@login_required(login_url='/login/login/')
def prestamos(request):
    clientdata = Cliente.objects.get(user_id = request.user.id)

    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
    except:
        accdata = None

    context = {'clientdata':clientdata, 'accdata':accdata}
    return render(request, 'clientes/prestamos.html', context)

@login_required(login_url='/login/login/')
def cotizaciones(request):
    clientdata = Cliente.objects.get(user_id = request.user.id)

    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
    except:
        accdata = None

    context = {'clientdata':clientdata, 'accdata':accdata}
    return render(request, 'clientes/cotizaciones.html', context)


class ClienteViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = ClienteSerializer
    def get_queryset(self):
        id = self.request.user.id
        return Cliente.objects.filter(user = id)

class CuentaViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CuentaSerializer
    def get_queryset(self):
        id = self.request.user.id
        user = Cliente.objects.filter(user = id)
        try:
            us_id = user[0].customer_id
            return Cuenta.objects.filter(customer_id = us_id)
        except:
            acc = []
            return acc