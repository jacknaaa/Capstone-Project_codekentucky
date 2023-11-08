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

print(df.shape)
print(df.head(10))