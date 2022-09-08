from django.db import models
from clientes.models import Cliente

class CardBrand(models.Model):
    card_brand_description = models.TextField()
    card_brand_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'card_brand'
class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, null=True, blank=True)
    card_number = models.CharField(max_length=20, unique=True)
    card_cvv = models.IntegerField()
    card_granted_date = models.CharField(max_length=20, null=True, blank=True)
    card_expiration_date = models.CharField(max_length=20, null=True, blank=True)
    card_brand = models.ForeignKey(CardBrand, models.DO_NOTHING, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tarjeta'