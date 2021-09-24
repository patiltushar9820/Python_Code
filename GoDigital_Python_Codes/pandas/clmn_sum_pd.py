#calculating sum of column using pandas
import pandas as pd
df=pd.read_csv('Book1.csv')
#print(df.Open.sum())

# print a single column values
#1 print(df['Open'])
#print(df.Open)

#comapare data column values with constant value
print(df.Open>2000)
