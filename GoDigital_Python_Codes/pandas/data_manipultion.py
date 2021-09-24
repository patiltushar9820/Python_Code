#data manipultion
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('Book1.csv')
#print(df.columns)#it returns the column names of the csv file 
#print(df.index)#It returns RangeIndex(start=0, stop=500, step=1)

#sort values 
#print(df.sort_values('Date'))

#subsetting multiple columns
#print(df[['Date','Open']])

#subsetting using .isin
#two_date_data=df['Date'].isin(['8/13/2019','8/9/2019'])
#print(df[two_date_data])

#add new column 
df['Hig_Low _Avg']=df["High"]-df["Low"]
print(df)