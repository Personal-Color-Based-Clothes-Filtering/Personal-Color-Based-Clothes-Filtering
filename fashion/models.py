from django.db import models
from .tone_extraction import ToneExtraction

# Create your models here.

# 파일 업로드
class FaceImage(models.Model) : 
    faceId = models.AutoField(primary_key=True)
    faceImg = models.ImageField(upload_to='images/') 

# MUSINSA
class Collar(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collar'
        

class Hoodie(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoodie'


class Longsleeve(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longsleeve'


class Shirt(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shirt'


class Shortsleeve(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shortsleeve'


class Sleeveless(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sleeveless'


class Sweat(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sweat'


class Sweater(models.Model):
    index = models.IntegerField(blank=True, primary_key = True)
    url = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    personal_color = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sweater'
    