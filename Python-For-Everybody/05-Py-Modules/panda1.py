
!pip install xlrd
!pip install openpyxl

import pandas as pd
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()

x = df[['Length']]
x
#column as 1D series


x = df[['Artist']]
type(x)