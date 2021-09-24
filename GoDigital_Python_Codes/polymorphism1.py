#polymorphism in python
class first:
    def first(self):
        print ('Tushar')
    def last(self):
        print('Patil')
class second:
    def first(self):
        print('Devesh')
    def last(self):
        print('jha')
obj1=first()
obj2=second()
for obj in (obj1,obj2):
    obj.first()
    obj.last()
    print('\n')
    