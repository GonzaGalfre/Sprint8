from msilib.schema import SelfReg
from rest_framework import serializers
from .models import Cliente
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