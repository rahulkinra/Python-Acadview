
#Ques 1
l=[]
n=int(input("Enter the number of integers\n"))
print("Enter the elements")
for i in range(n):
    b=int(input())
    l.append(b)
print(l)

#Ques 2
l2=['google','apple','facebook','microsoft','tesla']
l.extend(l2)
print(l)

#Ques 3
l3=[1,1,2,3,4,3,4,5,3,2,3,3]
print(l3.count(1))

#Ques 4
l4=[600,300,129,2,4,66,999,44,23,99,57,12]
l4.sort()
print(l4)

#Ques 5
a1=[1,10,2,4]
print("list 1 is: ",a1)
a2=[33,24,3,5,21,35]
print("list 2 is: ",a2)
a1.sort()
print("sorted list1 is: ",a1)
a2.sort()
print("sorted list2 is: ",a2)
a1.extend(a2)
print("merged is: ",a1)
a1.sort()
print("sorted + merged list is: ",a1)

#Ques 6
cEve=0
cOdd=0
for i in a1:
    if(i%2==0):
        cEve+=1
    else:
        cOdd+=1
print("Total Odd Count: " , cOdd)
print("Total Even Count: ",cEve)



#TUPLES

#Ques 1
di=[]
n = int(input("Enter total no. of elements in tuple\n"))
print("Enter integers")
for i in range(n):
    c=int(input())
    di.append(c)
t=tuple(di)
print("Tuple ->" , t)
rev=reversed(t)
print("Reversed tuple -> " , tuple(rev))

#Ques 2
k=[]
n = int(input("Enter total no. of elements in tuple\n"))
print("Enter integers")
for i in range(n):
    j=int(input())
    k.append(j)
p=tuple(k)
print("The largest and smallest elements are " , max(p) , " and " , min(p) , "respectively")



#STRINGS

#Ques 1
srt=input("Enter the string\n")
print(srt.upper())

#Ques 2
w=input("Enter a string\n")
count=0;
for i in range(len(w)):
    if w.isdigit():
       count=1;
    else:
        count=0;
        break;
if count==1:
    print("True")
else:
    print("False")

#Ques 3
xyz="Hello World"
print(xyz)
print(xyz.replace("World","Anonymous"))

