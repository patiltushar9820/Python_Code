#Bar graph in python
#horizontal bar graph
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('Book1.csv')
#plt.bar(df.Date,df.Open)
#plt.barh(df.Date,df.Open)

#stacked bar charts
plt.bar(df.Date,df.Close,label='Close')
plt.bar(df.Date,df.Open,bottom=df.Close,label='open')
plt.legend()
plt.show()