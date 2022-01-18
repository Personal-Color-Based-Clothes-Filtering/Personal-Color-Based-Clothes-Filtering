#카테고리별로 분리되어있는 csv파일들을 하나의 파일로 합친다.
import pandas as pd
import numpy as np
import os

# 파일들이 있는 폴더명으로 폴더내 파일 목록 확인
forders = os.listdir('../predataset')
print(forders)

df_all = pd.DataFrame()
for i in range(0,len(forders)):
    if forders[i].split('.')[1] == 'csv':
        file = '../predataset/'+forders[i]
        df= pd.read_csv(file,encoding='utf-8',index_col=0,nrows=500) 
        # df.drop(['Unnamed: 0'], axis = 1, inplace = True)
        df_all = pd.concat([df_all, df])

df_all.to_csv('../dataset/all.csv')