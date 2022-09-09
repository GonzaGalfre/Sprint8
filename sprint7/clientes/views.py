from http import client
from django.shortcuts import render
from .models import Cliente, Sucursal
from cuentas.models import Cuenta, Movimientos
from tarjetas.models import Tarjeta, CardBrand
from prestamos.models import Prestamo
from .serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer, SucursalSerializer, TarjetaSerializer, AllSucursalesSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser



# Create your views here.

@login_required(login_url='/login/login/')
def index(request):

    try:
        clientdata = Cliente.objects.get(user_id = request.user.id)
    except:
        clientdata = None
    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
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

class PrestamoViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PrestamoSerializer
    def get_queryset(self):
        id = self.request.user.id
        user = Cliente.objects.filter(user = id)
        try:
            us_id = user[0].customer_id
            return Prestamo.objects.filter(customer_id = us_id)
        except:
            loans = []
            return loans

class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SucursalSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        client_list = Cliente.objects.filter(branch_id = id)
        list = []
        loans = Prestamo.objects.all()
        for l in loans:
            for c in client_list:
                if l.customer_id == c.customer_id:
                    list.append(l)
        return list

class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class= TarjetaSerializer
    permission_classes= [IsAdminUser]
    lookup_field = 'customer_id'
    def get_queryset(self):
        id = self.kwargs['id']
        return Tarjeta.objects.filter(customer_id = id)

class ModifyLoansViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAdminUser]
    serializer_class = SucursalSerializer
    queryset = Prestamo.objects.all()
    lookup_field = 'loan_id'

    def get(self, request, format=None):
        prestamos = Prestamo.objects.all()
        serializer = SucursalSerializer(prestamos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PublicEndpoint(APIView):
    permission_classes = []

    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = AllSucursalesSerializer(sucursales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def inicio(request):
    return render(request, 'clientes/inicio.html')