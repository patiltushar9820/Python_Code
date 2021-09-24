#data visulization
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("Book1.csv")
df1=df.groupby("Date")["Open"].mean()
#df1.plot(kind="line")
#df1.plot(kind="bar")
#df.plot(x="Date",y="Open",kind="scatter")
#plt.legend()
#plt.show()
