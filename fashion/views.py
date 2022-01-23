# Create your views here.
from unicodedata import category
from django.shortcuts import render

# 무신사 데이터 가져오기
from .models import Clothes

def musinsa_fashion(request):
    # 톤 분류
    clothes = Clothes.objects.all().order_by('index')[:100]
    spring = Clothes.objects.filter(tone="spring")
    summer = Clothes.objects.filter(tone="summer")
    autumn = Clothes.objects.filter(tone="autumn")
    winter = Clothes.objects.filter(tone="winter")

    # 카테고리 분류
    collar = Clothes.objects.filter(category="collar")
    hoodie = Clothes.objects.filter(category="hoodie")
    shirt = Clothes.objects.filter(category="shirt")
    longsleeve = Clothes.objects.filter(category="longsleeve")
    shortsleeve = Clothes.objects.filter(category="shortsleeve")
    sleeveless = Clothes.objects.filter(category="sleeveless")
    sweat = Clothes.objects.filter(category="sweat")
    sweater = Clothes.objects.filter(category="sweater")

    return render(request, 'fashion/musinsa_view.html', 
    {'clothes': clothes, 
    'spring' : spring,
    'summer' : summer,
    'autumn' : autumn,
    'winter' : winter,

    'collar' : collar,
    'hoodie' : hoodie,
    'shirt' : shirt,
    'longsleeve' : longsleeve,
    'shortsleeve' : shortsleeve,
    'sleeveless' : sleeveless,
    'sweat' : sweat,
    'sweater' : sweater})




