from flask import Flask, render_template
import os
import pymongo
from bson.objectid import ObjectId

MONGODB_URI = 'mongodb+srv://Iftekhar:IA123456@30daysofpython.fqkqb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

#Creating a database and collection
db = client.thirty_days_of_python

#db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})

#Inserting many documents to collection
'''
students = [
    {'name': 'David', 'country':'UK', 'city': 'London', 'age': 34},
    {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
    {'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25},
]

for student in students:
    db.students.insert_one(student)
'''
#MongoDB Find
'''
student = db.students.find_one()
student = db.students.find_one({'_id':ObjectId('604856717fc61bab8511812d')})
'''
#students = db.students.find()
#students = db.students.find({}, {"_id": 0, "name": 1, "country": 1})
'''
query = {"age":{"$lt":30}}
students = db.students.find(query)
'''
'''
query = {'age': 250}
new_value = {'$set':{'age':38}}
'''
#students = db.students.find().limit(3)
#students = db.students.find().sort('name')
#db.students.update_one(query, new_value)
'''
query = {'name': 'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
'''
'''
students = db.students.find().sort('name', -1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age', -1)
for student in students:
    print(student)
'''
#print(client.list_database_names())
'''
app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
'''
db.students.drop()

