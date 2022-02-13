# Create your views here.
from django.shortcuts import render

# 무신사 데이터 가져오기
from .models import Clothes
from django.db.models import Q

def musinsa_fashion(request):
    clothes = Clothes.objects.all() # 전체
    tone = request.GET.get('tone', None)
    category = request.GET.get('category', None)
    color = request.GET.get('color', None)
    
    # 톤 분류
    if tone == "spring":
        personal_color = Clothes.objects.filter(tone="spring")
    elif tone == "summer":
        personal_color = Clothes.objects.filter(tone="summer")
    elif tone == "autumn":
        personal_color = Clothes.objects.filter(tone="autumn")
    elif tone == "winter":
        personal_color = Clothes.objects.filter(tone="winter")
    else:
        personal_color = Clothes.objects.all()

    # 카테고리 분류
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

    # 색상 분류
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
        
    q = Q() # 쿼리스트링

    # clothes = clothes.filter(
    # Q(tone=tone) |  
    # Q(category=category) | 
    # Q(lcolor=color) 
    # ).distinct()

    if tone:
        q &= Q(tone=tone)
    if category:
        q &= Q(category=category)
    if color:
        q &= Q(color=color)
    
    ctx = {
        'clothes': clothes
        ,'selected_color' : selected_color
        ,'personal_color' : personal_color
    }

    return render(request, 'fashion/musinsa_view.html', 
    context = ctx )




