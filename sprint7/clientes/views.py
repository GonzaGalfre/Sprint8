from django.shortcuts import render
from .models import Cliente
from cuentas.models import Cuenta, Movimientos
from tarjetas.models import Tarjeta, CardBrand
from django.contrib.auth.decorators import login_required



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