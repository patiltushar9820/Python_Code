#slicing the list in python using pandas
import pandas as pd
df=pd.read_csv("Book1.csv")
#1 print(df.loc[3:5])

#axis argument 
#df1=df.mean(axis="index")
#print(df1)

#axis argument 
df1=df.mean(axis="columns")
print(df1)
