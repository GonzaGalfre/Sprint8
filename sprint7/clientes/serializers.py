from rest_framework import serializers
from .models import Cliente
from cuentas.models import Cuenta

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['customer_id', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch_id']

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['account_id', 'balance']