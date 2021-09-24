#Explicit indexes
import pandas as pd
df=pd.read_csv("Book1.csv")
#df1=df.set_index('nm')
"""
df.reset_index()
df1=df.set_index(f'nm')
print(df1)

#drop index
print(df.reset_index(drop=True))

"""

#print(df[df["Date"].isin(["8/6/2021","8/5/2021"])])

#loc
#df1=df.loc[[0,1]]
#print(df1)

#multilevel indexes
df3=df.set_index(["first","second"])
print(df3)
