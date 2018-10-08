#Q.1- Write a python script to create a databse of students named Students.
import pymongo
client = pymongo.MongoClient()
data = client['Students1']
collection = data['Stud']

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
'''for i in range(10):
    name = input('Enter name')
    marks = int(input('Enter marks'))
    collection.insert_one({'Name':name,'Marks':marks})'''
d = collection.find()
for doc in d:
    print(doc)




#Q.4- Print the names of all the students who scored more than 80 marks.
print("Marks greater than 80 students are:")
p=collection.find({'Marks':{'$gt':80}})
for i in p:
print(i)
