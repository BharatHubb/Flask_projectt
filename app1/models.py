from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()


    class Meta:
        db_table = "prodcut"