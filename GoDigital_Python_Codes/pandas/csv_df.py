#creating dataframe to csv file and vice versa
import pandas as pd
df=pd.read_csv("Book1.csv")
df1=df.to_csv("new_csv.csv")
df_new=pd.read_csv("new_csv.csv")
print(df_new)