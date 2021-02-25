#Day 4: 30 days of python programming

#Problem 1
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
space = ' '
string1 = a + space + b + space + c + space + d

print(string1)

#Problem 2
a = 'Coding'
b = 'For'
c = 'All'
space = ' '
string2 = a + space + b + space + c

print(string2)

#Problem 3
company = 'Coding For All'

#Problem 4
print(company)

#Problem 5
print(len(company))

#Problem 6
print(company.upper())

#Problem 7
print(company.lower())

#Problem 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Problem 9
first_word = company[0:6]
print(first_word)

#Problem 10
print(company.index('Coding'))
print(company.find('Coding'))

#Problem 11
print(company.replace('Coding', 'Python'))

#Problem 12
string3 = 'Python for Everyone'
string4 = 'Python for All'

print(string3)
print(string3.replace(string3, string4))

#Problem 13
string5 = 'Coding For All'
print(string5.split(' '))

#Problem 14
string6 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string6.split(','))

#Problem 15
print(string5[0:1])

#Problem 16
print(string5[:-1])

#Problem 17
print(string5[9:10])

#Problem 18

#Problem 20
print(string5.index('C'))

#Problem 21
print(string5.index('F'))

#Problem 22
string7 = 'Coding For All People'
print(string7.rindex('l'))

#Problem 23
string8 = 'You cannot end a sentence with because because because is a conjunction'
print(string8.index('because'))

#Problem 24
print(string8.rindex('because'))

#Problem 25
print(string8[31:54])

#Problem 26
print(string8.find('because'))

#Problem 27
print(string8[31:54])

#Problem 28
print(string5.startswith('Coding'))

#Problem 29
print(string5.endswith('coding'))

#Problem 30
string9 = ' Coding For All  '
print(string9.strip(' '))

#Problem 31
string10 = '30DaysOfPython'
string11 = 'thirty_days_of_python'

print(string10.isidentifier())
print(string11.isidentifier())

#Problem 32
a = ['Django','Flask','Bottle','Pyramid','Falcon']
b = '# '.join(a)

print(b)

#Problem 33
string12 = 'I am enjoying this challenge'
string13 = 'I just wonder what is next'

print(string12 + '\n' + string13)

#Problem 34


#Problem 35
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with radius %d is %d meters square.' %(radius, area)

print(formated_string)

#Problem 36
