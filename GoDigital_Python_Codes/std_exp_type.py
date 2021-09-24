#exception hadling with standard exception types
import sys
def sqrt(x):
    """
        if x< 0:
        raise ValueError("X is less than zero "f"{x} is negative number")
    """
    guess=x
    i=0
    while guess * guess != x and i < 20:
        guess=(guess + guess / x) / 2.0
        i += 1
    return guess
def main():
    print(sqrt(9))
    try:
        print(sqrt(-1))
    except ValueError as e:
        print('you can not divide any number with zero',{e,sys.stderr})

if __name__=='__main__':
    main()