#카테고리별로 분리되어있는 csv파일들을 하나의 파일로 합친다.
import pandas as pd
import numpy as np
import os

def combine_csv():    
    forders = os.listdir('../finalDataset')
    df_all = pd.DataFrame()
    for i in range(0,len(forders)):
        if forders[i].split('.')[1] == 'csv':
            file = '../finalDataset/'+forders[i]
            df= pd.read_csv(file,encoding='utf-8',index_col=0,nrows=500) 
            # df.drop(['Unnamed: 0'], axis = 1, inplace = True)
            df_all = pd.concat([df_all, df])

    df_all.to_csv('../finalDataset/pre_clothes.csv')

def set_index():
    df = pd.read_csv('../finalDataset/pre_clothes.csv')
    for i in range(0,len(df)):
        df.loc[i,'index'] = int(i)
        print(df.loc[i,'index'])
    df.to_csv('../finalDataset/clothes.csv')

def delete_unnamed():
    df = pd.read_csv('../finalDataset/clothes.csv',index_col=1)
    df.drop(['Unnamed: 0'], axis = 1, inplace = True)
    df.to_csv('../finalDataset/clothes.csv')

combine_csv()
set_index()
delete_unnamed()