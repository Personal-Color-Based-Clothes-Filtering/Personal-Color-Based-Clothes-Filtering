import cv2
import numpy as np

def FaceDetect():
  # 이미지 파일 읽기
  img = cv2.imread("./face/personal_color_check/image/cropped.jpg", cv2.IMREAD_COLOR)

  img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  # 잡음 제거
  img_hsv = cv2.fastNlMeansDenoisingColored(img_hsv,None,10,10,7,21)

  lower = np.array([0,48,80], dtype="uint8") #부호없는 8비트 정수형
  upper = np.array([20,255,255], dtype="uint8")
  img_person = cv2.inRange(img_hsv, lower, upper) #살색 범위를 출력

  #경계선 찾음
  contours, hierarchy = cv2.findContours(img_person, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) 
  #_, contours, hierarchy = cv2.findContours(img_person, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  
  # 가장 큰 영역 찾기
  max = 0
  maxcnt = None
  for cnt in contours :
      area = cv2.contourArea(cnt)
      if(max < area) :
          max = area
          maxcnt = cnt

  #maxcontours의 각 꼭지점 다각선 만들기 
  hull = cv2.convexHull(maxcnt)

  # 같은 크기의 배경 검정색인 이미지 만들기
  mask = np.zeros(img.shape).astype(img.dtype)
  color = [255, 255, 255]
  # 경계선 내부 흰색으로 채우기
  cv2.fillPoly(mask, [maxcnt], color)

  img_person = cv2.bitwise_and(img, mask)

  cv2.imwrite("./face/personal_color_check/image/skincolor_face.jpg", img_person)
  print("2")


def Check():
  while True:
    image_color = cv2.imread("./face/personal_color_check/image/skincolor_face.jpg", cv2.IMREAD_COLOR)
    image_color = cv2.cvtColor(image_color, cv2.COLOR_BGR2LAB)

    height,width = image_color.shape[:2] #이미지를 저장할 넘파이 배열 생성

  #픽셀 접근방법: for 루프를 돌면서 (x,y)에 있는 픽셀을 하나씩 접근한다.
    count = 0
    count_invalid =0 

    for y in range(0, height):
      for x in range(0, width):
        #컬러이미지의 (x,y)픽셀에 있는 픽셀의 l,a,b채널을 읽는다
        l = image_color.item(y,x,0)
        a = image_color.item(y,x,1)
        b = image_color.item(y,x,2)

        #lab가 검정이 아닐때 (검정에 가깝거나 흰색에 가까운 회색 포함)
        if l*100/255 >= 48 and l*100/255 < 80 and a-128 != 0 and b-128 !=0: 
          count+=1
        
        if not (l*100/255 >= 48 and l*100/255 < 80 and a-128 != 0 and b-128 !=0):
          count_invalid += 1
        
    if count_invalid/(count_invalid + count) > 0.7:
      print("unsuccessful processing")
      return "fail"
  
    else:
      print("successful processing")
      return "successful processing"

Check()