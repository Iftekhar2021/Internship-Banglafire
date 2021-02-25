"""
#Examples
lst = list()

empty_list = list()
print(len(empty_list))

lst = []
empty_list = []
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print(last_index)
print(last_fruit)

first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]

print(first_fruit)
print(last_fruit)
print(second_last)

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst

print(first_item)
print(second_item)
print(third_item)
print(rest)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits

print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

first, second, third, *rest, ninth, tenth = [1,2,3,4,5,6,7,8,9,10]

print(first)
print(second)
print(third)
print(rest)
print(ninth)
print(tenth)

countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries

print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]

print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(reverse_fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) 
does_exist = 'lime' in fruits
print(does_exist)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
'''del fruits
print(fruits)'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

fruits = ['banana', 'orange', 'mango', 'lemon']
#fruits.reverse()
print(fruits.reverse()) #printing None
ages = [22, 19, 24, 25, 26, 24, 25, 24]
#ages.reverse()
print(ages.reverse()) #printing None

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)
"""

#Exercises: Level 1

#Problem 1
empty_list = []
print(empty_list)

#Problem 2
list1 = ['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Nepal', 'Bhutan', 'Maldives']
print(list1)

#Problem 3
print(len(list1))

#Problem 4
first_item = list1[0]
middle_item = list1[3]
last_item = list1[6]

print(first_item)
print(middle_item)
print(last_item)

#Problem 5
mixed_data_types = ['Iftekharul Alam', 20, 175, 'Unmarried', 'Bangladesh']
print(mixed_data_types)

#Problem 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Problem 7
print(it_companies)

#Problem 8
no_of_companies = len(it_companies)
print(no_of_companies)

#Problem 9
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[6]

print(first_company)
print(middle_company)
print(last_company)

#Problem 10
it_companies[0] = 'Banglafire'
print(it_companies)

#Problem 11
it_companies.append('Facebook')
print(it_companies)

#Problem 12
it_companies.insert(4, 'Uber')
print(it_companies)

#Problem 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#Problem 14
print('#; '.join(it_companies))

#Problem 15
does_exist = 'Banglafire' in it_companies
print(does_exist)
does_exist = 'BANGLAFIRE' in it_companies
print(does_exist)

'''
#Problem 16
print(it_companies.sort()) #printing None

#Problem 17
print(it_companies.reverse()) #printing None
'''

#Problem 18
print(it_companies[3:])

#Problem 19
print(it_companies[:-3])

#Problem 20
print(it_companies[4:5])

#Problem 21
del it_companies[0]
print(it_companies)

#Problem 22
del it_companies[3:5]
print(it_companies)

#Problem 23
del it_companies[-1]
print(it_companies)

#Problem 24
del it_companies[0:]
print(it_companies)

#Problem 25
del it_companies

#Problem 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end + back_end

#Problem 27
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#Exercises: Level 2
#Problem 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(len(ages))

min_age = ages[0]
max_age = ages[9]
print(min_age)
print(max_age)

ages.insert(0, 19)
ages.insert(11, 26)
print(ages)

median_age = int((ages[5] + ages[6]) / 2)
print(median_age)

average_age = sum(ages) / 12
print(average_age)

range_of_ages = max_age - min_age
print(range_of_ages)

value1 = abs(min_age - average_age)
value2 = abs(max_age - average_age)

print(value1-value2)

#Another Problem 1
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

print(len(countries))

middle_country = countries[96]
print(middle_country)

#Problem 2
first_half = countries[0:97]
second_half = countries[98:193]

print(first_half)
print(second_half)

#Problem 3
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries2

print(first_country)
print(second_country)
print(third_country)
print(scandic_countries)

