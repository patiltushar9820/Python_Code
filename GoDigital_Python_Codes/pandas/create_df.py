#creating dataframes
import pandas as pd
#list of dictionaries
list_of_dicts=[
    {'name':'Ginger','bread':'dachshund','height_cm':22,'weight':10,'date_of_birth':'1998-03-20'},
     {'name':'scout','bread':'dalmatian','height_cm':26,'weight':80,'date_of_birth':'1996-03-20'}
]
print(pd.DataFrame(list_of_dicts))

#dictionaries of list
dict_of_lists={
    'name':['Ginger','scout'],
    'bread':['dachshund','dalmatian']
}
print(pd.DataFrame(dict_of_lists))