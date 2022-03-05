import pandas as pd
import cv2
import numpy as np
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

from tone_extraction import *

pd.set_option('mode.chained_assignment',  None)
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('../finalDataset/clothes.csv', index_col = 0)
i = 0
for url in df.loc[:,'thumbnail']:
  try:
    res = urlopen(url)
    if res.status == 200 or res.status != 404:
      try:
        tone_extraction_instance = ToneExtraction(url)
        tone = tone_extraction_instance.extract_tone()

        df.loc[i,'tone'] = tone 
      except: 
        df.drop([i],axis=0)
    else:
      df.drop([i],axis=0)
      
  except HTTPError as e:
    err = e.read()
    code = e.getcode()

  i += 1
  
#df.drop(['Unnamed: 0'], axis = 1, inplace = True)
df.to_csv('../finalDataset/ex3.csv')

