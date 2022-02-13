import cv2
import dlib
import matplotlib.pyplot as plt
import numpy as np
import os 

def Resize(img) :
    
  width = 800
  ratio = width/img.shape[1] # width * 사진 너비 = 비율
  height = int(ratio*img.shape[0]) # 비율 * 사진 높이

  resize = cv2.resize(img, dsize = (width, height), interpolation = cv2.INTER_AREA)
  return resize

def CropFace():
  # 이미지 파일 읽기
  try:
    image_list = os.listdir('media/images/') # media/images 폴더 내 저장된 파일명 불러오기 
    img = cv2.imread("media/images/" + image_list[-1], cv2.IMREAD_COLOR)
    
    cv2.imwrite("./media/origin/original.jpg", img)
    image_url = '/media/origin/original.jpg'
    # cv2.imwrite("./face/personal_color_check/image/original.jpg", img)
    # image_url = '/face/personal_color_check/image/original.jpg'

    # 이미지 사이즈 조정 
    img = Resize(img)

    try:
      # 얼굴 검출기와 랜드마크 검출기 생성 --- ①
      detector = dlib.get_frontal_face_detector()

      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      # 얼굴 영역 검출 --- ②
      faces = detector(gray)

      #얼굴영역 추출 후 사진 저장
      for f in faces:
        crop = img[f.top():f.bottom(), f.left():f.right()]
      cv2.imwrite("./face/personal_color_check/image/cropped.jpg", crop)
      return image_url
    
    except:
      return "fail"
    
  except:
    return "fail"

CropFace()