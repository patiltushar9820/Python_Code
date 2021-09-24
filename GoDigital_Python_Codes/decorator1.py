#decorator
def ordinary():
    print('i am ordinary')

#decorator
def second(func):
    def inner():
        print('i am in decorator function now ')
        #here again function decorate its output
        func()
    return inner
