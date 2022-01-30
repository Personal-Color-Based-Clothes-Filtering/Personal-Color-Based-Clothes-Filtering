from django.db import models


# MUSINSA
class Clothes(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    tone = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clothes'