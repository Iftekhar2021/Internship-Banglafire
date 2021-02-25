#Day 3: 30 days of python programming
age = 20
height = 175.00
complex_var = 1 + 1j

#Problem 4
base = float(input('Enter base: '))
height = float(input('Enter height: '))

area = 0.5 * base * height

print('The area of the triangle is ', int(area))

#Problem 5
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

perimeter = a + b + c

print('The perimeter of the triangle is ', perimeter)

#Problem 6
length = float(input('Enter length: '))
width = float(input('Enter width: '))

area = length * width
perimeter = 2 * (length + width)

print('The area of the rectangle is ', area)
print('The perimeter of the rectangle is ', perimeter)

#Problem 7
r = float(input('Enter radius: '))
pi = 3.14

area = pi * r * r
c = 2 * pi * r

print('The area of the circle is ', area)
print('The circumference of the circle is ', c)

#Problem 13
print(('on' in 'python') and ('on' in 'jargon')) 

#Problem 14
print('jargon' in 'I hope this course is not full of jargon')

#Problem 15
print(not(('on' in 'dragon') and ('on' in 'python')))

#Problem 16
length = len('python')

print(length)
print(float(length))
print(str(length))

#Problem 17
number = int(input('Enter a number: '))

if (number % 2) == 0:
    print('Number is even')
else:
    print('Number is not even')

#Problem 18
print((7 // 3) == (int(2.7)))

#Problem 19
print(type('10') == type(10))

#Problem 20
print(int(9.8) == 10)

#Problem 21
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
earning = hours * rate_per_hour

print('Your weekly earning: ', earning)

#Problem 22
years = int(input('Enter number of years you have lived: '))

lived = years * 365 * 24 * 60 * 60

print('You have lived for', lived, 'seconds')

#Problem 23

