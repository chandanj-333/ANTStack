from django.db import models

# Create your models here.
class Item(models.Model):
    item=models.CharField(blank=False,max_length=50)
    itemCategory=models.CharField(blank=False,max_length=20)
    quantity=models.IntegerField(blank=False)
    price=models.IntegerField(blank=False)
