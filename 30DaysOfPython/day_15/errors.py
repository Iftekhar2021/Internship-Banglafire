#Examples
#SyntaxError
#print 'hello world'
print ('hello world')

#NameError
#print(age)
age = 25
print(age)

#IndexError
numbers = [1, 2, 3, 4, 5]
#print(numbers[5])
print(numbers[4])

#ModuleNotFoundError
#import maths
import math

#AttributeError
import math
#print(math.PI)
print(math.pi)

#KeyError
users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
#print(users['county'])
print(users['country'])

#TypeError
#print(4 + '3')
print(4 + int('3'))
print(4 + float('3'))

#ImportError
#from math import power
from math import pow
print(pow(2, 3))

#ValueError
#print(int('12a'))

#ZeroDivisionError
print(1 / 0)