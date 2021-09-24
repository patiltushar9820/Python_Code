#scatter plot in python
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('Book1.csv')
plt.scatter(df.Date,df.Close,alpha=1)
plt.show()
