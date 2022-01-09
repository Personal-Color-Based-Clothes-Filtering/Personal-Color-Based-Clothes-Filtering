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


# 얼굴 사진 업로드
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import FaceImage

def face_image_view(request):
    form = FaceForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        pass
    return render(request, 'fashion/upload_image.html', {'form' : form })


 # 퍼스널 컬러 판단
from .crop_face import *
from .rm_eye_lips import *
from .roi_cheek import *
from .models import FaceImage

def success(request):
    faceimg = CropFace()
    RmEyeLips()
    roi = RoiCheek()
    return render(request, 'fashion/personal_color.html', {'roi' : roi, 'faceimg' : faceimg})


# 첫 화면
from django.shortcuts import render
def main(request):
    return render(request, 'fashion/main_page.html')

