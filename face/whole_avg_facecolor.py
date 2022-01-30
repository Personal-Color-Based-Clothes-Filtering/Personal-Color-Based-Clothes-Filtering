import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag

while True:

  image_color = cv.imread("./face/personal_color_check/image/removed_eyes.jpg", cv.IMREAD_COLOR)
  image_color = cv.cvtColor(image_color, cv.COLOR_BGR2LAB)
  img_result = image_color.copy()

  height,width = image_color.shape[:2] #이미지를 저장할 넘파이 배열 생성

#픽셀 접근방법: for 루프를 돌면서 (x,y)에 있는 픽셀을 하나씩 접근한다.
  count = 0 
  mean_l= 0
  mean_a= 0
  mean_b= 0
  for y in range(0, height):
    for x in range(0, width):
      #컬러이미지의 (x,y)픽셀에 있는 픽셀의 l,a,b채널을 읽는다
        l = image_color.item(y,x,0)
        a = image_color.item(y,x,1)
        b = image_color.item(y,x,2)

        #lab가 검정이 아닐때 (검정에 가깝거나 흰색에 가까운 회색 포함)
        if l*100/255 >= 48 and l*100/255 < 80 and a-128 != 0 and b-128 !=0: 
          count+=1
          mean_l += l 
          mean_a += a 
          mean_b += b

  mean_l = (mean_l/count)*100/255
  mean_a = mean_a/count-128
  mean_b = mean_b/count-128

  # print("mean_l:", round(mean_l, 2), " mean_a:", round(mean_a, 2), " mean_b:", round(mean_b,2))
  
  # if mean_a>=mean_b and mean_a-mean_b>=2:
  #   print("당신은 여름 쿨톤입니다.\n")
  # elif mean_a>=mean_b and mean_a-mean_b<2:
  #   print("당신은 겨울 쿨톤입니다.\n")
  # elif mean_a<mean_b and mean_l>64:
  #   print("당신은 봄 웜톤입니다.\n")
  # else:
  #   print ("당신은 가을 웜톤입니다.\n")
  break