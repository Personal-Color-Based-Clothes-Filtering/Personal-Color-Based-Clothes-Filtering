import cv2
import dlib
import matplotlib.pyplot as plt
import numpy as np
import os 


def DelImg():
  # 이미지 파일 읽기
  try:
    image_list = os.listdir('media/images/') # media/images 폴더 내 저장된 파일명 불러오기 
    image_url = "media/images/" + image_list[-1]

    return os.remove(image_url)

  except:
    pass

DelImg()