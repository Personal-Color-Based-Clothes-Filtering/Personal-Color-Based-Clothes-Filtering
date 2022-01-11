# Create your views here.
from django.shortcuts import render

# 무신사 데이터 가져오기
from .models import Clothes

def musinsa_fashion(request):
    clothes = Clothes.objects.all().order_by('index')[:100]

    return render(request, 'fashion/musinsa_view.html', {'clothes': clothes})




