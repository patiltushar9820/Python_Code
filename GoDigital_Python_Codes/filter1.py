#filter function in python
# it always returns a list as a output 
#syntax filter(func,seq)
def filter_func(variable):
    vowel=['a','e','i','o','u']
    if variable in vowel:
        return True
    else:
        return False
seq=['a','b','c','d','e','e','i']
filter1=filter(filter_func,seq)
print('founded vowel are\n')
for i in filter1:
    print(i)
