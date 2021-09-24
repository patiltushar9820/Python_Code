import pandas as pd 
from matplotlib import  pyplot as plt
df=pd.read_csv('Book1.csv')
#plot graph
#gives a labels to axis
plt.xlabel("Date")
plt.ylabel("Open")
#plt.text(4,5,"hi ")
plt.plot(df.Date,df.Open,label='Graph')
plt.show()

#show info about file data
#print(df.info())