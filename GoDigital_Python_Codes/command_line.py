#command line arguments first
import sys
def first_name():
    return 'Tushar'
def last_name():
    return 'Patil'
def print_full_name(name):
    print(name)
def main():
    first_nm=sys.argv[1]
    last_nm=sys.argv[2]
    name=first_nm+' '+last_nm
    print_full_name(name)

if(__name__)=='__main__':
    main()
