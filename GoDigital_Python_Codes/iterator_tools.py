#iterator tools
#any()
#all()
#zip
#chain
import itertools
from itertools import chain
first=['1','2','3']
second=['4','5','6']
third=['3','6','9']
for item in zip(first,second):
    print(item)
for temp in zip(first,second,third):
    print(f"min:{min(temp)},max:{max(temp)}")
print('\n chain module operation',list(chain(first,second,third)))