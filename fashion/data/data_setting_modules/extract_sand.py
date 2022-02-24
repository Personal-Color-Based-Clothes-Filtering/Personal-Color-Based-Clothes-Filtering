import pandas as pd
import os

#csv를 읽는다.
#category별로 행을 읽는다.
#해당 행들을 따로 모은다. https://hogni.tistory.com/9
#원본에서 행을 제거하고, 다른 파일로 저장한다.
#다른 csv파일로 저장한다.
def get_sand():
    df = pd.read_csv('../dataset/clothes (2).csv')

    is_sand = df['color'] == 29
    sand = df[is_sand]

    sand.to_csv('../predataset/sand.csv',index=False)
def set_index():
    df = pd.read_csv('../predataset/sand.csv')
    for i in range(0,len(df)):
        df.loc[i,'index'] = int(i)
        print(df.loc[i,'index'])
    df.to_csv('../midDataset/sand.csv',index=False)

set_index()