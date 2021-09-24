#histogram in python
import pandas as pd 
from matplotlib import pyplot as plt
df=pd.read_csv('Book1.csv')
#plt.hist(df.Open)

#histogram with range(min, max) value
#plt.hist(df.Open,range=(1000,2000))

#two histogram on same page
plt.hist(df.Open,density=1,label='Open')
plt.hist(df.Close,density=1,label='Close')
plt.legend()
plt.show()

