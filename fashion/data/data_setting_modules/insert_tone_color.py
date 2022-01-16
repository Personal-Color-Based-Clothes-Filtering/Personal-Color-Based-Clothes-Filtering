#color,tone 컬럼을 생성한 다음,각 컬럼에 색상명과 tone 정보를 삽입한다.
#삽입 후 최종 csv 반환하여 dataset 폴더에 저장한다.
import pandas as pd
import cv2
import numpy as np
import urllib.request
from tone_extraction import *

#경고 안뜨게 설정
pd.set_option('mode.chained_assignment',  None)

df = pd.read_csv('../dataset/clothes.csv', index_col = 0)
# 이상한 열 제거
# df.drop(['Unnamed: 0.1'], axis = 1, inplace = True)
# df.drop(['Unnamed: 0.1.1'], axis = 1, inplace = True)
# print(df)
# df.to_csv('../dataset/dataset3.csv')

# 데이터 삽입
for i in range(0,len(df)):
    if df['thumbnail'][i]:  
      url = df['thumbnail'][i]
      print(url)
      tone_extraction_instance = ToneExtraction(url)
      tone,color = tone_extraction_instance.extract_tone()

      print(i,',df["tone"]:',tone)
      print(i,',df["color"]:',color)
      df['tone'][i] = tone 
      df['color'][i] = color

df.to_csv('../dataset/final_dataset.csv')

