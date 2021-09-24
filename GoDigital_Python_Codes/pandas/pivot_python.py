#pivot table in python 
import pandas as pd
import numpy as np
df=pd.read_csv("Book1.csv")
print(df.pivot_table(values="Open",index="Date"))

#pivot table with multiple values 
#print(df.pivot_table(values="Open",index="Date",aggfunc=[np.mean,np.median]))

#pivot on two variable
print(df.pivot_table(values="Open",index="Date",columns="Close"))

#fill missing value in pivot table 
print(df.pivot_table(values="Open",index="Date",columns="Close",fill_value=0))

#get average of open and close values in last column
print(df.pivot_table(values="Open",index="Date",columns="Close",fill_value=0,margins=True))
 
