from django.db import models

# Create your models here.


class InventoryappOrdertbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    totalprice = models.IntegerField(db_column='TotalPrice')  # Field name made lowercase.
    date = models.CharField(max_length=100)
    productid = models.ForeignKey('InventoryappProduct', models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = False
        db_table = 'inventoryapp_ordertbl'


class InventoryappProduct(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventoryapp_product'


class InventoryappSuppliertbl(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=100)  # Field name made lowercase.
    productid = models.ForeignKey(InventoryappProduct, models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = False
        db_table = 'inventoryapp_suppliertbl'