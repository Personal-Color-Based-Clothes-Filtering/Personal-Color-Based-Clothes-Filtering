from django.shortcuts import render
import random

# 무신사 데이터 가져오기
from .models import Clothes
from django.db.models import Q

def musinsa_fashion(request):
    clothes = Clothes.objects.all() # 전체
    
    # 톤 분류
    tone = request.GET.get('tone', None)

    if tone == "spring":
        personal_color = Clothes.objects.filter(tone="spring")
    elif tone == "summer":
        personal_color = Clothes.objects.filter(tone="summer")
    elif tone == "autumn":
        personal_color = Clothes.objects.filter(tone="autumn")
    elif tone == "winter":
        personal_color = Clothes.objects.filter(tone="winter")

    # 색상 분류
    color = request.GET.get('color', None)

    if color == "3":
        selected_color = Clothes.objects.filter(color="3")
    elif color == "11":
        selected_color = Clothes.objects.filter(color="11")
    elif color == "10":
        selected_color = Clothes.objects.filter(color="10")
    elif color == "12":
        selected_color = Clothes.objects.filter(color="12")
    elif color == "9":
        selected_color = Clothes.objects.filter(color="9")
    elif color == "6":
        selected_color = Clothes.objects.filter(color="6")
    elif color == "7":
        selected_color = Clothes.objects.filter(color="7")
    elif color == "8":
        selected_color = Clothes.objects.filter(color="8")
    elif color == "4":
        selected_color = Clothes.objects.filter(color="4")
    elif color == "29":
        selected_color = Clothes.objects.filter(color="29")
    else:
        selected_color = Clothes.objects.all()

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
    if color:
        q &= Q(color=color)
    if tone:
        q &= Q(tone=tone)
    
    # ctx = {
    #     'clothes': clothes,
    #     'selected_color' : selected_color,
    #     'personal_color' : personal_color
    # }

    return render(request, 'fashion/musinsa_view.html', 
    {'clothes': clothes,
    'selected_color' : selected_color
    })
    #'context' = ctx )




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