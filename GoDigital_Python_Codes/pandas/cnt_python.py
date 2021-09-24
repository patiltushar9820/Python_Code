#counting in python
import pandas as pd
df=pd.read_csv('Book1.csv')
print(df.drop_duplicates(subset="Open"))#drop duplicates Open value data entry 
print(df["Open"].value_counts())#it counts how many entries of each Open value in data
print(df["Open"].value_counts(sort=True))#it counts how many entries of each Open value in data and sort it also 