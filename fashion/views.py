# Create your views here.
from django.shortcuts import render
import random
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator

# 무신사 데이터 가져오기
from .models import Clothes
from django.db.models import Q

def all_list(request):
    clothes = Clothes.objects.all() # 전체

    num = random.randrange(1, 200)
    num_range = num + 8

    print(num,num_range)
    # 톤 분류
    spring = Clothes.objects.filter(tone="spring")[num:num_range]
    summer = Clothes.objects.filter(tone="summer")[num:num_range]
    autumn = Clothes.objects.filter(tone="autumn")[num:num_range]
    winter = Clothes.objects.filter(tone="winter")[num:num_range]

    return render(request, 'fashion/all_list.html', 
    {'spring' : spring, 'summer' : summer, 'autumn' : autumn, 'winter' : winter})

def spring_list(request):
    clothes = Clothes.objects.filter(tone="spring")
    category = request.GET.get('category',None)
    color = request.GET.get('color',None)

    if category != None or color != None:
        
        q = Q(tone='spring')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
    
        clothes = Clothes.objects.filter(q).distinct()
        clothes_serialized = serializers.serialize('json',clothes)
        return JsonResponse(clothes_serialized,safe=False)

    page = request.GET.get('page','1')
    paginator = Paginator(clothes,80)
    page_obj = paginator.get_page(page)
    print(category,color,page_obj)

    return render(request,'fashion/spring_list.html',{
        'clothes':page_obj
    })

def summer_list(request):
    clothes = Clothes.objects.filter(tone="summer")

    category = request.GET.get('category',None)
    color = request.GET.get('color',None)

    if category != None or color != None:
        
        q = Q(tone='summer')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
    
        clothes = Clothes.objects.filter(q).distinct()
        clothes_serialized = serializers.serialize('json',clothes)
        return JsonResponse(clothes_serialized,safe=False)

    return render(request,'fashion/summer_list.html',{
        'clothes':clothes
    })

def summer_list(request):
    clothes = Clothes.objects.filter(tone="summer")

    category = request.GET.get('category',None)
    color = request.GET.get('color',None)

    if category != None or color != None:
        
        q = Q(tone='summer')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
    
        clothes = Clothes.objects.filter(q).distinct()
        clothes_serialized = serializers.serialize('json',clothes)
        return JsonResponse(clothes_serialized,safe=False)

    return render(request,'fashion/summer_list.html',{
        'clothes':clothes
    })

def autumn_list(request):
    clothes = Clothes.objects.filter(tone="autumn")

    category = request.GET.get('category',None)
    color = request.GET.get('color',None)

    if category != None or color != None:
        
        q = Q(tone='autumn')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
    
        clothes = Clothes.objects.filter(q).distinct()
        clothes_serialized = serializers.serialize('json',clothes)
        return JsonResponse(clothes_serialized,safe=False)

    return render(request,'fashion/autumn_list.html',{
        'clothes':clothes
    })

def winter_list(request):
    clothes = Clothes.objects.filter(tone="winter")

    category = request.GET.get('category',None)
    color = request.GET.get('color',None)

    if category != None or color != None:
        
        q = Q(tone='winter')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
    
        clothes = Clothes.objects.filter(q).distinct()
        clothes_serialized = serializers.serialize('json',clothes)
        return JsonResponse(clothes_serialized,safe=False)

    return render(request,'fashion/winter_list.html',{
        'clothes':clothes
    })