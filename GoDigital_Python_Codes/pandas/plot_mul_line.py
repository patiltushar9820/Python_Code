#plot multiple lines on same graph
#legend
#linewidth is used for to set width of line
#linestyle
#marker
#style

import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('Book1.csv')
plt.plot(df.Date,df.Open,label="Date vs Open",color="tomato")#color set the color to line
plt.plot(df.Date,df.Close,label="Date vs Close",color="orange",linewidth=1,linestyle=':',marker='o')
plt.style.use('ggplot')
plt.legend()
plt.show()
