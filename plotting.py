import pandas as pd 
import seaborn as sns
sns.set(color_codes=True)
import matplotlib.pyplot as plt

df=pd.DataFrame(pd.read_csv("data\shopping_trends_updated.csv"))

# Customer shopping trend
# def Most Popular Items():
# Most Purchased Item in Each Age Group
# most_popular_categories
# Item Purchases by Males
# Item Purchases by Females


    


def most_popular_categories():
    categories_count=df["Category"].value_counts()
    # print(categories_count)
    # Category
    # Clothing       1737
    # Accessories    1240
    # Footwear        599
    # Outerwear       324
    # Name: count, dtype: int64

    # Plotting a pie chart Most Popular Categories
    plt.figure(figsize=(10, 10))
    plt.pie(categories_count, labels=categories_count.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("viridis"))
    plt.title('Most Popular Categories')
    plt.show()