#here i pass fuction as parameter to another function
import sys
def first_name():
    return 'Tushar'
def last_name():
    return 'Patil'
def print_full_name(first_name,last_name):
    name=first_name+' '+last_name
    print(name)
def main():
    nm=sys.argv[1]
    print(nm)
if(__name__)=='__main__':
    main()
