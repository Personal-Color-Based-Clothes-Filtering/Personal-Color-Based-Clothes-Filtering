import cv2 as cv
import numpy as np
from imutils import face_utils
import dlib
from .whole_avg_facecolor import mean_l, mean_a, mean_b
# from whole_avg_facecolor import mean_l, mean_a, mean_b

def RoiCheek():
  #face detection part
  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

  image_color = cv.imread("./face/personal_color_check/image/cropped.jpg", cv.IMREAD_COLOR)
  
  gray_img = cv.cvtColor(image_color, cv.COLOR_BGR2GRAY)
  lab_img = cv.cvtColor(image_color, cv.COLOR_BGR2LAB)

  #rect is the face detected
  faces = detector(gray_img)
  for rect in faces:
    # 얼굴 영역을 좌표로 변환 --- ③
    x,y = rect.left(), rect.top()
    w,h = rect.right()-x, rect.bottom()-y
  
    # 얼굴 랜드마크 검출 --- ④
    shape = predictor(gray_img, rect)
    for i in range(68):
        # 부위별 좌표 추출 및 표시 --- ⑤
        part = shape.part(i)
        cv.circle(gray_img, (part.x, part.y), 2, (0, 0, 255), -1)
        cv.putText(gray_img, str(i), (part.x, part.y), cv.FONT_HERSHEY_PLAIN, \
                                         0.5,(255,255,255), 1, cv.LINE_AA)

  shape = predictor(gray_img, rect)
  shape = face_utils.shape_to_np(shape)

  #ROI 영역을 구해서 평균을 구한다.
  img_roi = lab_img[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]] #right cheek
  img_roi2 = lab_img[shape[29][1]:shape[33][1], shape[54][0]:shape[13][0]] #left cheek (사진 기준)
  m = cv.mean(img_roi) #오른쪽 뺨
  m2 = cv.mean(img_roi2) #왼쪽 뺨

  #ROI에 대한 평군 픽셀값으로 채운 이미지를 생성한다. #영역을 roi로 해야 에러 미발생
  img_mean = np.zeros(img_roi.shape, dtype=np.uint8) #평균색 이미지를 저장할 넘파이 배열을 생성한다
  img_mean2 = np.zeros(img_roi2.shape, dtype=np.uint8)
  
  img_mean[:] = (m[0], m[1], m[2])
  img_mean2[:] = (m2[0], m2[1], m2[2])
  L = m[0]*100/255
  a = m[1]-128
  b = m[2]-128
  L2 = m2[0]*100/255
  a2 = m2[1]-128
  b2 = m2[2]-128
  

  weigh_l = round((mean_l*0.8 + L*0.1 + L2*0.1),2)
  weigh_a = round((mean_a*0.8 + a*0.1 + a2*0.1),2)
  weigh_b = round((mean_b*0.8 + b*0.1 +b2*0.1),2)
  
  if weigh_a>=weigh_b and weigh_a-weigh_b>=2:
    return "여름 쿨톤"
  elif weigh_a>=weigh_b and weigh_a-weigh_b<2:
    return "겨울 쿨톤"
  elif weigh_a<weigh_b and weigh_l>=65.15:
    return "봄 웜톤"
  elif weigh_a<weigh_b and weigh_a>=12.8:
    return "겨울 쿨톤"
  else:
    return "가을 웜톤"
