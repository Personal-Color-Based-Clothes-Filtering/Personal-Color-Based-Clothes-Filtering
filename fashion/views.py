# Create your views here.
from django.shortcuts import render

# 무신사 데이터 가져오기
from .models import Collar
from .models import Hoodie
from .models import Longsleeve
from .models import Shirt
from .models import Shortsleeve
from .models import Sleeveless
from .models import Sweat
from .models import Sweater

def musinsa_fashion(request):
    collar = Collar.objects.all().order_by('index')[:12]
    hoodie = Hoodie.objects.all().order_by('index')[:12]
    shirt = Shirt.objects.all().order_by('index')[:12]
    longsleeve = Longsleeve.objects.all().order_by('index')[:12]
    shortsleeve = Shortsleeve.objects.all().order_by('index')[:12]
    sleeveless = Sleeveless.objects.all().order_by('index')[:12]
    sweat = Sweat.objects.all().order_by('index')[:12]
    sweater = Sweater.objects.all().order_by('index')[:12]
    return render(request, 'fashion/musinsa_view.html', {'collar': collar, 'hoodie': hoodie, 'longsleeve': longsleeve,
                                                    'shirt': shirt, 'shortsleeve': shortsleeve, 'sleeveless': sleeveless,
                                                     'sweat': sweat, 'sweater': sweater})




