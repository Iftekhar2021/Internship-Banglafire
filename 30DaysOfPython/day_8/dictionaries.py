'''
#Example
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(person)
print(len(person))
print(person['first_name'])
print(person['last_name'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
#print(person['city'])

print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city', 'City is not found'))
print(person.get('JavaScript'))

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

person['first_name'] = 'Eyob'
person['age'] = 25
print(person)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)
print('key5' in dct)

dct.pop('key1')
print(dct)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()
print(dct)

del dct['key2']
print(dct)

person.pop('first_name')
person.popitem()
del person['is_married']
print(person)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
print(dct.clear())
print(dct)
del dct

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)

keys = dct.keys()
print(keys)

values = dct.values()
print(values)
'''

#Exercises
#Problem 1
dog = {}
print(dog)

#Problem 2
dog = {
    'name':'Pluto',
    'color':'White',
    'breed':'',
    'legs':'',
    'age':5
}
print(dog)

#Problem 3
student = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'gender':'Male',
    'age':250,
    'marital status':'Unmarried',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Finland',
    'city':'Helsinki',
    'address':{
        'street':'Space street',
        'zip_code': '02110'
    }
}
print(student)

#Problem 4
print(len(student))

#Problem 5
print(student['skills'])
print(type(student['skills']))

#Problem 6
student['skills'].append('HTML')
print(student['skills'])

#Problem 7
keys = student.keys()
print(keys)

#Problem 8
values = student.values()
print(values)

#Problem 9
print(student.items())

#Problem 10
student.pop('first_name')
print(student)

#Problem 11
del student

