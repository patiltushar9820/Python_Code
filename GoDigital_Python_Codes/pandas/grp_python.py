#summaries by group
import pandas as pd
df=pd.read_csv("Book1.csv")
print(df[df["Date"]=="8/11/2021"]["Open"].mean())
print(df[df["Date"]=="8/10/2021"]["Open"].mean())

#groupby method in pathon for grouping data 
print(df.groupby("Date")["Open"].mean)

#multiple group by 
print(df.groupby("Date")["Open"].agg([min,max,sum]))

#
print(df.groupby(["Date","Close"])["Open"].mean())
