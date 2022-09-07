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
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    card_number = models.IntegerField(unique=True)
    card_cvv = models.IntegerField()
    card_granted_date = models.IntegerField()
    card_expiration_date = models.IntegerField()
    card_brand = models.ForeignKey(CardBrand, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'