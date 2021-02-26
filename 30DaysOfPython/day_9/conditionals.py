'''
#Examples
a = 3
if a > 0:
    print('A is a positive number')

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

a = 3
print('A is positive') if a > 0 else print('A is negative')

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is positive and even integer')
    else:
        print('A is a positive number')

elif a == 0:
    print('A is zero')
else:
    print('A is negative number')

a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer') 
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')

#Exercises
#Problem 1
user_input = int(input("Enter your age: "))
print(user_input)

if user_input >= 18:
    print('You are old enough to learn to drive.')
else:
    wait = 18 - user_input
    print('You need', wait, 'more years to learn to drive.')

#Problem 2:
my_age = 20
your_age = int(input("Enter your age: "))

if your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print('You are', age_difference, 'year older than me.')
    else:
        print('You are', age_difference, 'years older than me.')
elif your_age < my_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print('You are', age_difference, 'year younger than me.')
    else:
        print('You are', age_difference, 'years younger than me.')
else:
    print('You are of the same age as me')

#Problem 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is smaller than', b)
else:
    print(a, 'and', b, 'are equal')

#Problem 4
score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
    print('Your grade is A')
elif score >= 70 and score <= 79:
    print('Your grade is B')
elif score >= 60 and score <= 69:
    print('Your grade is C')
elif score >= 50 and score <= 59:
    print('Your grade is D')
else:
    print('Your grade is F')

#Problem 5
month = input("Enter month: ").capitalize()

if month == 'September' or month == 'October' or month == 'November':
    print("The season is Autumn.")
elif month == 'December' or month == 'January' or month == 'February':
    print("The season is Winter.")
elif month == 'March' or month == 'April' or month == 'May':
    print("The season is Spring.")
else:
    print("The season is Summer.")

#Problem 6
fruits = ['banana', 'orange', 'mango', 'lemon']
enter_fruit = input("Enter fruit name: ").lower()

if enter_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(enter_fruit)
    print(fruits)
'''
#Problem 7
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'Java', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02110'
    }
}
'''
if person.get('skills'):
    length = len(person['skills'])
    if length % 2 != 0:
        item = length // 2
        print(person['skills'][item])
    else:
        item1 = int(length / 2)
        item2 = int((length / 2) - 1)
        print(person['skills'][item1], person['skills'][item2])
'''
if 'skills' in person:
    if ('skills' == 'Python'):
        print('Python' in 'skills')
    else:
        print("Python is not found in 'skills'")
else:
    print("'skills' is not found in person")


