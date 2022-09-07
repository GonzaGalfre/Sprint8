from django.db import models
from clientes.models import Cliente


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'

class AccountType(models.Model):
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    account_type_id = models.AutoField(primary_key=True)
    account_tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_type'

class Movimientos(models.Model):
    account = models.ForeignKey(Cuenta, models.DO_NOTHING)
    amount = models.IntegerField()
    transaction_type = models.TextField()
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'