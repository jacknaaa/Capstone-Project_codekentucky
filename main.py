import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

## Path CSV files ##
# kaggle\input\archive\shopping_trends.csv
# kaggle\input\archive\shopping_trends_updated.csv

# shape file shopping_trends_updated.csv
trends=pd.read_csv("data\shopping_trends_updated.csv")

df=pd.DataFrame(trends)
df.shape

# print(df.shape)
# print(df.head(10))
print(df.info()) 
print(df.isnull().sum()) #to check null data nad Dtype
##### INFO #####
# Data columns (total 18 columns):
#  #   Column                  Non-Null Count  Dtype
# ---  ------                  --------------  -----
#  0   Customer ID             3900 non-null   int64
#  1   Age                     3900 non-null   int64
#  2   Gender                  3900 non-null   object
#  3   Item Purchased          3900 non-null   object
#  4   Category                3900 non-null   object
#  5   Purchase Amount (USD)   3900 non-null   int64
#  6   Location                3900 non-null   object
#  7   Size                    3900 non-null   object
#  8   Color                   3900 non-null   object
#  9   Season                  3900 non-null   object
#  10  Review Rating           3900 non-null   float64
#  11  Subscription Status     3900 non-null   object
#  12  Shipping Type           3900 non-null   object
#  13  Discount Applied        3900 non-null   object
#  14  Promo Code Used         3900 non-null   object
#  15  Previous Purchases      3900 non-null   int64
#  16  Payment Method          3900 non-null   object
#  17  Frequency of Purchases  3900 non-null   object
# dtypes: float64(1), int64(4), object(13)
# memory usage: 548.6+ KB

