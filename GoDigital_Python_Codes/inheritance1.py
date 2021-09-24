#inheritance in python 
#
class person:
    def __init__(self,id,number):
        self.id=id
        self.number=number
    def display(self):
        print(self.id)
        print(self.number)
class emp(person):
    def __init__(self,id,number,name):
        self.name=name
        person.__init__(self,id,number)
a=emp(1,123,'tushar')
a.display()