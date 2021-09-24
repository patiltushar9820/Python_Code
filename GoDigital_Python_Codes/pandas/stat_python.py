#statistics in python
#mean
import pandas as pd
df=pd.read_csv('Book1.csv')
print("mean of the Open values :",df['Open'].mean())
print("median of the Open values :",df['Open'].median())
print("mode of the Open values :",df['Open'].mode())
print("min of the Open values :",df['Open'].min())
print("max of the Open values :",df['Open'].max())
print("variance of the Open values :",df['Open'].var())
print("standard deviation of the Open values :",df['Open'].std())
print("Sum of the Open values :",df['Open'].sum())
def pct30(column):
    return column.quantile(0.3)
print("Aggregate of the Open values :",df['Open'].agg(pct30))
print("Cumultive sum of the open values :",df['Open'].cumsum())
print("Cumultive min of the open values :",df['Open'].cummin())
print("Cumultive max of the open values :",df['Open'].cummax())
print("Cumultive product of the open values :",df['Open'].cumprod())