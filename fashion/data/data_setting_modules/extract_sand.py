import pandas as pd
import os

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