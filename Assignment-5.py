#ques 1
year = int(input("Please Enter the Year Number you wish: "))
 
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)

#Ques 2
length=float(input("Enter length\n"))
breadth=float(input("Enter breadth\n"))
if(length==breadth):
    print("It is a square")
else:
    print("It is a rectangle")

#ques 3
x=int(input("Enter age of person 1\n"))
y=int(input("Enter age of person 2\n"))
z=int(input("Enter age of person 3\n"))
print("Oldest person is ",max(x,y,z)," years old\nYoungest person is ",min(x,y,z)," Years old")

#Ques 4
a=int(input("Enter age\n"))
s=input("Enter M if Male and F if female\n")
m=input("Enter Y if married and N if not married\n")
if(s=='F' or s=='f'):
    print("She will work only in urban areas\n")
elif(s=='M'or s=='m' and (a>19 and a<41)):
    print("He may work anywhere")
elif(s=='M' or s=='m' and (a>39 and a<61)):
    print("He will work in urban areas only")
else:
    print("Error")

#ques 5
cost=100
q=int(input("Enter quantity\n"))
p=float(q*cost)
if(q>1000):
    j=float(0.1*p)
    val=float(p-j)
    print("Cost after discount is ",val)
else:
    print("Sorry no discount amount is ",p)
    
#ques 6
for i in range(0,10):
    n=int(input("Enter integer "))
    print(n)

#OR

b=[]
for i in range(0,10):
    n=int(input("Enter integer "))
    b.append(n)
print(b)
    
#ques 7
while(True):
    print("Lets Rock ✌")

#ques  8
num=int(input("How many elements do you want to enter\n"))
lst=[]
for i in range(0,num):
    h=int(input("Enter the element\n"))
    lst.append(h)
lst2=[]
for i in lst:
    h=i*i
    lst2.append(h)
print(lst2)

#ques 9
a=[]
b=[]
c=[]
l=[4,5,6,7,8,'a','b','c','d',5.00,6.00,8.098]
for i in l:
    if(type(i) is str):
        a.append(i)
    elif(type(i) is float ):
        b.append(i)
    elif(type(i) is int):
        c.append(i)
print("List of integer type : ",c)
print("List of float type : ",b)
print("List of string type : ",a)

#ques 10
lst=[]
for i in range(1,101):
    count=0
    for j in range(2, int(i/2)) :
        if(i%j==0):
            count+=1
    if(count==0):
        lst.append(i)
print(lst)

#ques 11
k='*'
for i in range(1,5):
    print(i*k)
    
#ques 12
l1=[]
num=int(input("how may elements in list?\n"))
for i in range(0,num):
    h=input("Enter element")
    l1.append(h)
hi=input("Which element you want\n")
l1.remove(hi)
print(l1)
