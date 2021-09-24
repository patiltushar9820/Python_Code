#reduce function in python
#for use reduce function in program you required functools
import functools
list1=[1,2,3,4]
print(functools.reduce(lambda x,y:x+y  , list1))