import cv2
import dlib
import matplotlib.pyplot as plt
import numpy as np
import os 

def Resize(img) :
    #print(img.shape)
    width = 800
    ratio = width/img.shape[1] # width * 사진 너비 = 비율
    height = int(ratio*img.shape[0]) # 비율 * 사진 높이

    # 축소 INTER_AREA
    # 확대 INTER_LINEAR
    resize = cv2.resize(img, dsize = (width, height), interpolation = cv2.INTER_AREA)
    # resize = cv2.resize(img, dsize = (0, 0), fx=1.5, fy=1.5, interpolation = cv2.INTER_AREA)
    # print(resize.shape) 
    return resize

def CropFace():
  # 이미지 파일 읽기
  image_list = os.listdir('./media/images') # media/images 폴더 내 저장된 파일명 불러오기 
  img = cv2.imread("./media/images/" + image_list[-1], cv2.IMREAD_COLOR)
  image_url = "/media/images/" + image_list[-1]

  # 이미지 사이즈 조정 
  img = Resize(img)

  # 얼굴 검출기와 랜드마크 검출기 생성 --- ①
  detector = dlib.get_frontal_face_detector()
  #predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

  #img = cv2.imread("./images/me.jpg")
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # 얼굴 영역 검출 --- ②
  faces = detector(gray)

  #얼굴영역 추출 후 사진 저장
  for f in faces:
    crop = img[f.top():f.bottom(), f.left():f.right()]
  cv2.imwrite("./fashion/personal_color_check/image/cropped.jpg", crop)

  return image_url

CropFace()