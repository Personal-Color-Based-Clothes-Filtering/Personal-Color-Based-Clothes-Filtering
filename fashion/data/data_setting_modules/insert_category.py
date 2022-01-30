#csv 데이터의 카테고리 칼럼을 추가하고, category 데이터를 집어넣는다. 
import pandas as pd

df = pd.read_csv('../predataset/sweat.csv')
df['category'] = 'sweatshirt'
df.head()
df.to_csv('../dataset/sweatshirt.csv')

# df = pd.read_csv('../dataset/all.csv')
# df['tone'] = 'spring'
# df['color'] = 'red'
# df.head()
# df.to_csv('../dataset/all.csv')