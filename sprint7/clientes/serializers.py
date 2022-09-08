from msilib.schema import SelfReg
from rest_framework import serializers

from tarjetas.models import Tarjeta
from .models import Cliente, Sucursal
from cuentas.models import Cuenta
from prestamos.models import Prestamo

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['customer_id', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch_id']

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['account_id', 'balance']

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_total', 'loan_date', 'loan_type']

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_total', 'loan_date', 'loan_type', 'customer_id']

class TarjetaSerializer(serializers.ModelSerializer):
    customer_id = serializers.ReadOnlyField(source='customer_id.customer_id')
    class Meta:
        model = Tarjeta
        fields = ['customer_id', 'card_id', 'card_number', 'card_cvv', 'card_expiration_date']

class AllSucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"