#lambda
#1

numbers=(1,2,3,4)
(lambda number:print(numbers))(numbers)

#2
lambda_square=lambda x:x * x
print(lambda_square(3))

#3 lambda function with list comprehension
lambda2=[lambda x=x:x*x for x in range(1,10)]
for table in lambda2:
    print(table())