#Q.1- Write a python script to create a databse of students named Students.
import sqlite3
con = sqlite3.connect('Students.db')
print("Created")
con.close()

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    '''query = 'create table stud(name varchar(20),marks number(3))'
    print('Created')
    cursor.execute(query)'''
    for i in range(10):
        print("Enter name " , i , " and marks " , i)
        n = input()
        m = int(input())
        query = 'insert into stud(name,marks) values(?,?)'
        cursor.execute(query,(n,m))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

#Q.4- Print the names of all the students who scored more than 80 marks.
try:
    con = sqlite3.connect('Students.db')
    cur = con.cursor()
    query = 'Select * from stud where marks>80'
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print('Name: {} , Marks: {}'.format(row[0], row[1]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cur:
        cur.close()
    if con:
        con.close()
