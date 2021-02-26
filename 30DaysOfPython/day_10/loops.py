#Examples
'''count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print(letter)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")
print('outside the loop')

lst = list(range(11))
print(lst)
st = set(range(1, 11))
print(st)

lst = list(range(0, 11, 2))
print(lst)
st = set(range(0, 11, 2))
print(st)
for number in range(11):
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for number in range(11):
    print(number)
else:
    print('The loop stops at', number)

for number in range(6):
    pass
'''
#Exercises
#Problem 1
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for number in numbers:
    print(number)
    number = number + 1

number = 0
while number < 11:
    print(number)
    number = number + 1

#Problem 2
for number in range(10, -1, -1):
    print(number)

number = 10
while number >= 0:
    print(number)
    number = number - 1

#Problem 3
hashes = '#'
while len(hashes) < 8:
    print(hashes)
    hashes = hashes + '#' 
'''
#Problem 4
hashes2 = '#'
while len(hashes2) < 16:
    print(hashes)
    hashes = hashes + ' #'
'''
#Problem 5
for number in range(0, 11):
    print(number, 'x', number, '=', number ** 2)

#Problem 6
skills = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skill in skills:
    print(skill)

#Problem 7
for number in range (0, 101, 2):
    print(number)

#Problem 8
for number in range(1, 100, 2):
    print(number)

#Problem 9
sum = 0
for number in range(0, 101):
    sum = sum + number
print(sum)

#Problem 10
even_sum = 0
odd_sum = 0

for number in range(0, 101, 2):
    even_sum = even_sum + number

for number in range(1, 100, 2):
    odd_sum = odd_sum + number

print("The sum of all evens is", even_sum, ". And the sum of all odds is", odd_sum,".")

'''
#Problem 11
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Problem 12
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    print(fruit)
'''