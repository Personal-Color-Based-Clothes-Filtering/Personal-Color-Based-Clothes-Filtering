# Create your views here.
from django.shortcuts import render
import random
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator

from .models import Clothes
from django.db.models import Q

def all_list(request):
    clothes = Clothes.objects.all()

    num = random.randrange(1, 200)
    num_range = num + 8

    spring = Clothes.objects.filter(tone="spring")[num:num_range]
    summer = Clothes.objects.filter(tone="summer")[num:num_range]
    autumn = Clothes.objects.filter(tone="autumn")[num:num_range]
    winter = Clothes.objects.filter(tone="winter")[num:num_range]

    return render(request, 'fashion/all_list.html', 
    {'spring' : spring, 'summer' : summer, 'autumn' : autumn, 'winter' : winter})

def spring_list(request):
    clothes = Clothes.objects.filter(tone="spring").order_by('index')
    category = request.GET.get('category',None)
    color = request.GET.get('color',None)
    print(category,color)

    if category != None or color != None:
        q = Q(tone='spring')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
        clothes = Clothes.objects.filter(q).distinct()

    page = request.GET.get('page','1')
    paginator = Paginator(clothes,48)
    page_obj = paginator.get_page(page)
    print(category,color,page_obj)

    return render(request,'fashion/spring_list.html',{
        'clothes':page_obj,
        'category':category,
        'color':color
    })

def summer_list(request):
    clothes = Clothes.objects.filter(tone="summer").order_by('index')
    category = request.GET.get('category',None)
    color = request.GET.get('color',None)
    print(category,color)

    if category != None or color != None:
        q = Q(tone='summer')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
        clothes = Clothes.objects.filter(q).distinct()

    page = request.GET.get('page','1')
    paginator = Paginator(clothes,48)
    page_obj = paginator.get_page(page)
    print(category,color,page_obj)

    return render(request,'fashion/summer_list.html',{
        'clothes':page_obj,
        'category':category,
        'color':color
    })

def autumn_list(request):
    clothes = Clothes.objects.filter(tone="autumn").order_by('index')
    category = request.GET.get('category',None)
    color = request.GET.get('color',None)
    print(category,color)

    if category != None or color != None:
        q = Q(tone='autumn')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
        clothes = Clothes.objects.filter(q).distinct()

    page = request.GET.get('page','1')
    paginator = Paginator(clothes,48)
    page_obj = paginator.get_page(page)
    print(category,color,page_obj)

    return render(request,'fashion/autumn_list.html',{
        'clothes':page_obj,
        'category':category,
        'color':color
    })

def winter_list(request):
    clothes = Clothes.objects.filter(tone="winter").order_by('index')
    category = request.GET.get('category',None)
    color = request.GET.get('color',None)
    print(category,color)

    if category != None or color != None:
        q = Q(tone='winter')
        if category and category != 'all':
            q &= Q(category=category)
            print(category)
        if color and color != 'all':
            q &= Q(color=color)
            print(color)
        clothes = Clothes.objects.filter(q).distinct()

    page = request.GET.get('page','1')
    paginator = Paginator(clothes,48)
    page_obj = paginator.get_page(page)
    print(category,color,page_obj)

    return render(request,'fashion/winter_list.html',{
        'clothes':page_obj,
        'category':category,
        'color':color
    })