import pandas as pd
import os

def devide_csv():
    df = pd.read_csv('../dataset/clothes.csv')

    is_collar = df['category'] == 'collar'
    is_hoodie = df['category'] == 'hoodie'
    is_longsleeve = df['category'] == 'longsleeve'
    is_shirt = df['category'] == 'shirt'
    is_shortsleeve = df['category'] == 'shortsleeve'
    is_sleeveless = df['category'] == 'sleeveless'
    is_sweat = df['category'] == 'sweat'
    is_sweater = df['category'] == 'sweater'

    collar = df[is_collar]
    hoodie = df[is_hoodie]
    longsleeve = df[is_longsleeve]
    shirt = df[is_shirt]
    shortsleeve = df[is_shortsleeve]
    sleeveless = df[is_sleeveless]
    sweat = df[is_sweat]
    sweater = df[is_sweater]

    collar.to_csv('../predataset/collar.csv')
    hoodie.to_csv('../predataset/hoodie.csv')
    longsleeve.to_csv('../predataset/longsleeve.csv')
    shirt.to_csv('../predataset/shirt.csv')
    shortsleeve.to_csv('../predataset/shortsleeve.csv')
    sleeveless.to_csv('../predataset/sleeveless.csv')
    sweat.to_csv('../predataset/sweat.csv')
    sweater.to_csv('../predataset/sweater.csv')

def cut_csv():
    filePath = '../predataset/'
    fileAll = os.listdir(filePath)

    for file in fileAll:
        df = pd.read_csv(filePath + file, header=None, nrows = 500)
        df.to_csv('../dataset/'+file,index=False, header=False)

cut_csv()