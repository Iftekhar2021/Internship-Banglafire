#Examples
tpl = ('item1', 'item2', 'item3', 'item4')

all_items = tpl[0:4]
print(all_items)

all_items = tpl[0:]
print(all_items)

middle_two_items = tpl[1:3]
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[0:4]
print(all_fruits)

all_fruits = fruits[0:]
print(all_fruits)

orange_mango = fruits[1:3]
print(orange_mango)

orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)

tpl = ('item1', 'item2', 'item3', 'item4')

all_items = tpl[-4:]
print(all_items)

middle_two_items = tpl[-3:-1]
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[-4:]
print(all_fruits)

orange_mango = fruits[-3:-1]
print(orange_mango)

orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)

fruits = ('banana', 'orange', 'mango', 'lemon')

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)

fruits = tuple(fruits)
print(fruits)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
#fruits[0] = 'apple' #gives an error because tuple cannot be modified

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

print(fruits_and_vegetables)

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

#Exercises

#Problem 1
empty_tuple = tuple()
print(empty_tuple)

#Problem 2
brothers = ('Donald Trump', 'Joe Biden', 'Narendra Modi', 'Imran Khan')
sisters = ('Sheikh Hasina', 'Khaleda Zia')

#Problem 3
siblings = brothers + sisters
print(siblings)

#Problem 4
print(len(siblings))

#Problem 5
siblings = list(siblings)
print(siblings)

siblings.append('Bill Clinton')
siblings.append('Hillary Clinton')
print(siblings)

family_members = tuple(siblings)
print(family_members)

#Problem 6
siblings = family_members[0:6]
print(siblings)

parents = family_members[6:8]
print(parents)

#Problem 7
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('potato', 'onion', 'carrot')
animal_products = ('meat', 'milk')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Problem 8
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Problem 9
middle_item = food_stuff_lt[4:5]
print(middle_item)

#Problem 10
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[6:9]
print(first_three_items)
print(last_three_items)

#Problem 11
del food_stuff_tp

#Problem 12
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
