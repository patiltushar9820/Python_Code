#missing values in python 
import pandas as pd
df=pd.read_csv("Book1.csv")
df1=df.pivot_table(values="Open",index="Date",columns="Close")
 

#1 print(df1.isna())
#2 print(df1.isna().any())
#3 print(df1.isna().sum())
#print(df1)