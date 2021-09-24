#class in python
#define a class in python
#pass is word like placeholder in python
class flight1:
   
    def number123(self):
        return "self._number123"
    def __init__(self, number123):
        if not number123[:2].isalpha():\
            raise ValueError(F"no airline code in code'{number123}'")
        self._number123 = number123
"""
    output of the above code
    >>> import class1
    >>> from class1 import flight1
    >>> fg=flight1()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: __init__() missing 1 required positional argument: 'number123'
    >>> fg=flight1('welcome')
    >>> fg.number123()
    'self._number123'
    >>> fg._number123
    'welcome'

    raise ValueError(F"no airline code in code'{number123}'")
ValueError: no airline code in code'123'
"""
#here i passed the value to initilizer
class Aircraft:
    def __init__(self,registration,model,num_rows,num_sets_per_row):
        self._registration=registration
        self._model=model
        self._num_rows=num_rows
        self._num_seat_per_row=num_sets_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model
    def seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seat_per_row])