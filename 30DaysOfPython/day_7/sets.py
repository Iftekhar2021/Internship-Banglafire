#Examples
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon))

print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))
print(python.issubset(dragon))

print(whole_numbers.difference(even_numbers))
print(python.difference(dragon))
print(dragon.difference(python))

some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))
print(python.symmetric_difference(dragon))

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))
print(python.isdisjoint(dragon))

#Exercises
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Problem 1
print(len(it_companies))

#Problem 2
it_companies.add('Twitter')
print(it_companies)

#Problem 3
it_companies.update(['Tesla', 'SpaceX'])
print(it_companies)

#Problem 4
it_companies.remove('IBM')
print(it_companies)

#Problem 6
print(A.union(B))

#Problem 7
print(A.intersection(B))

#Problem 8
print(A.issubset(B))

#Problem 9
print(A.isdisjoint(B))

#Problem 10
print(A.union(B))
print(B.union(A))

#Problem 11
print(A.symmetric_difference(B))

#Problem 12
del A
del B

#Problem 13
ages = set(age)
print(ages)
print(len(age))
print(len(ages))

#Problem 15
words = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
unique_words = set(words)
print(unique_words)
print(len(unique_words))




