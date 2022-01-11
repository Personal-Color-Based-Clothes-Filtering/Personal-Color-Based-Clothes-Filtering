from django.shortcuts import render
from django.urls import reverse

# 얼굴 사진 업로드
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import FaceImage
 # 퍼스널 컬러 판단
from .crop_face import *
from .rm_eye_lips import *
from .roi_cheek import *
from .models import FaceImage

def face_image_view(request):
    form = FaceForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('success'))
    else:
        pass
    return render(request, 'face/face_upload.html', {'form' : form })


def success(request):
    faceimg = CropFace()
    RmEyeLips()
    roi = RoiCheek()
    return render(request, 'face/face_result.html', {'roi' : roi, 'faceimg' : faceimg})