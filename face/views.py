from ast import Del
import imp
from urllib import request
from django.shortcuts import render
from django.urls import reverse
import cv2 as cv

# 얼굴 사진 업로드
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import FaceImage
 # 퍼스널 컬러 판단
from .crop_face import *
from .face_detect import *
from .rm_eye_lips import *
from .roi_cheek import *
from .delete_img import *
from .models import FaceImage

def face_image_view(request):
    form = FaceForm(request.POST, request.FILES)
    print('save')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print('save')
            return redirect('/face/success')
    else:
        pass
    return render(request, 'face/face_upload.html', {'form' : form })


def success(request):
    faceimg = CropFace()
    FaceDetect()
    check = Check()
    RmEyeLips()
    image_color = cv.imread("./face/personal_color_check/image/cropped.jpg", cv.IMREAD_COLOR)
    roi = RoiCheek(image_color)
    check2 = Check2()
    DelImg()
    Reset()
    # if roi == 'fail':
    #     pass
    return render(request, 'face/face_result.html', {'check' : check, 'check2' : check2, 'roi' : roi, 'faceimg' : faceimg})