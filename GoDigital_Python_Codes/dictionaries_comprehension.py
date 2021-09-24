#dictionaries comprehension
#comprehensions do not have any side effects
dict1={'name':'tushar','cmp':'godigital'}
print('normal dict :',dict1)
dict2={info1:header1 for header1,info1 in dict1.items()}
print('after swapping new dict is :',dict2)
dict3={info2[0]:header2 for info2,header2 in dict1.items()}
print('\n updated dict. is :',dict3)