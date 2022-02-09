from django.shortcuts import render
import random

# 무신사 데이터 가져오기
from .models import Clothes
from django.db.models import Q

def musinsa_fashion(request):
    clothes = Clothes.objects.all() # 전체
    
    # 톤 분류
    spring = Clothes.objects.filter(tone="spring")
    summer = Clothes.objects.filter(tone="summer")
    autumn = Clothes.objects.filter(tone="autumn")
    winter = Clothes.objects.filter(tone="winter")

    # 카테고리 분류
    category = request.GET.get('category', None)

    if category == "collar":
        clothes = Clothes.objects.filter(category="collar")
    elif category == "hoodie":
        clothes = Clothes.objects.filter(category="hoodie")
    elif category == "longsleeve":
        clothes = Clothes.objects.filter(category="longsleeve")
    elif category == "shirt":
        clothes = Clothes.objects.filter(category="shirt")
    elif category == "shortsleeve":
        clothes = Clothes.objects.filter(category="shortsleeve")
    elif category == "sleeveless":
        clothes = Clothes.objects.filter(category="sleeveless")
    elif category == "sweat":
        clothes = Clothes.objects.filter(category="sweat")
    elif category == "sweater":
        clothes = Clothes.objects.filter(category="sweater")
    else:
        clothes = Clothes.objects.all() # 전체

    q = Q() # 쿼리스트링
    if category:
        q &= Q(category=category)
    


    return render(request, 'fashion/musinsa_view.html', 
    {'clothes': clothes, 
    'spring' : spring,
    'summer' : summer,
    'autumn' : autumn,
    'winter' : winter

    # 'collar' : collar,
    # 'hoodie' : hoodie,
    # 'shirt' : shirt,
    # 'longsleeve' : longsleeve,
    # 'shortsleeve' : shortsleeve,
    # 'sleeveless' : sleeveless,
    # 'sweat' : sweat,
    # 'sweater' : sweater
    })




def all_list(request):
    clothes = Clothes.objects.all() # 전체

    num = random.randrange(1, 401)
    numRange = num + 4

    print(num,numRange)
    # 톤 분류
    spring = Clothes.objects.filter(tone="spring")[num:numRange]
    summer = Clothes.objects.filter(tone="summer")[num:numRange]
    autumn = Clothes.objects.filter(tone="autumn")[num:numRange]
    winter = Clothes.objects.filter(tone="winter")[num:numRange]

    return render(request, 'fashion/all_list.html', 
    {'spring' : spring, 'summer' : summer, 'autumn' : autumn, 'winter' : winter})