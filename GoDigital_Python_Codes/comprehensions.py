#comprehensions

#comprehensions are conccise of syntax for describing list, set and dictinories
#it same as natural language
#comprehension are written in square bracket
import math
from math import factorial

llist1="welcome in go digital".split()
print(llist1)
print("print len of every string using comprrehension",[len(i) for i in llist1])
print("\n set comprehension :")
set1={len(str(ii)) for ii in range(10)}
print(set1)
"""
    >> set1={len(str(i)) for i in range(10)}
    >>> type(set1)
    <class 'set'>
    >>> set1
    {1}
"""