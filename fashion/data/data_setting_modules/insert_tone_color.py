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

df = pd.read_csv('../dataset/clothes.csv', index_col = 0)

print('df타입:',type(df))
print('길이:',len(df))

# 데이터 삽입
i = 0
for url in df.loc[:,'thumbnail']:
  print(url,':',type(url))
  try:
    res = urlopen(url)
    print(res.status)
    if res.status == 200 or res.status != 404:
      tone_extraction_instance = ToneExtraction(url)
      tone = tone_extraction_instance.extract_tone()
      # color = tone_extraction_instance.get_color_name()

      print(i,',df["tone"]:',tone)
      # print(i,',df["color"]:',color)
      df.loc[i,'tone'] = tone 
      # df.loc[i,'color'] = color
    else:
      df.drop([i],axis=0)
  except HTTPError as e:
    err = e.read()
    code = e.getcode()
    print(code) ## 404
    df.drop([i],axis=0)

  i += 1

df.to_csv('../dataset/insert_tone_dataset.csv')

