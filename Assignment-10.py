#Q.1- Write a Python program to read n lines of a file
from itertools import islice
n = int(input("Enter how much lines of file you want to read? "))
try:
    f = open('Ques1.txt','r')
    lines = f.readlines(n)
    for i in islice(f,n):
        print(i)
    f.close()
except FileNotFoundError:
    print("File not found")

#Q.2- Write a Python program to count the frequency of words in a file.
try:
    from collections import Counter
    f = open('Ques2.txt','r')
    data = f.read()
    dit = Counter(data.split())
    print(dit)
    f.close()
except FileNotFoundError:
    print('file not found')

#Q.3- Write a Python program to copy the contents of a file to another file.
try:
    f1 = open('Ques2.txt')
    f2 = open('Ques3.txt','w')
    data = f1.read()
    f2.write(data)
    f1.close()
    f2.close()
except FileNotFoundError:
    print('File not found')

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
try:
    print('hi')
    with open('Ques2.txt') as ff1, open('Ques4.txt') as ff2:
        items = zip(ff1,ff2)
        for li1,li2 in items:
            print(li1+li2)
except FileNotFoundError:
    print('File not found')

#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random

with open("random1.txt","w+") as f:
    for i in range(10):
        f.write(str(random.randint(0,9)))
        f.write("\n")
with open("random1.txt") as f1,open("random2.txt","w+") as f2:
    l = []
    for line in f1:
        l.append(int(line.strip("\n")))
    l = sorted(l)
    for i in l:
        f2.write(str(i)+"\n")
with open("random2.txt") as f:
    for i in f:

        print(i.strip("\n"))
