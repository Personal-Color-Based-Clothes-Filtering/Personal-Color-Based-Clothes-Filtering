#color,tone 컬럼을 생성한 다음,각 컬럼에 색상명과 tone 정보를 삽입한다.
#삽입 후 최종 csv 반환하여 dataset 폴더에 저장한다.
import pandas as pd
import cv2
import numpy as np
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

from tone_extraction import *

#경고 안뜨게 설정
pd.set_option('mode.chained_assignment',  None)
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('../dataset/sweater.csv', index_col = 1)

# 데이터 삽입
i = 0
for url in df.loc[:,'thumbnail']:
  print(url,':',type(url))
  try:
    res = urlopen(url)
    print(res.status)
    #품절 상품이 아니면
    if res.status == 200 or res.status != 404:
      try:
        tone_extraction_instance = ToneExtraction(url)
        tone = tone_extraction_instance.extract_tone()

        print(i,',df["tone"]:',tone)
        df.loc[i,'tone'] = tone 
      except: 
        df.drop([i],axis=0)
    else:
      df.drop([i],axis=0)
      
  except HTTPError as e:
    err = e.read()
    code = e.getcode()
    print(code) ## 404
    df.drop([i],axis=0)

  i += 1
  
df.drop(['Unnamed: 0'], axis = 1, inplace = True)
df.to_csv('../finalDataset/sweater_insert_tone.csv')

