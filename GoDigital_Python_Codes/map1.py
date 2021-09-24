#map function in python 
#map function returns a result in list format
def addition(a):
    return a*a;
numbers=(1,2,3)
list1=map(addition,numbers)
print(list(list1))    

#map with lambda function
lambada1=lambda x:x * x
list2=map(lambada1,numbers)
print(list(list2))