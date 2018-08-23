#Ques 1
list=[]
n=int(input("how many elements"))
for i in range(0,n):
    a=input("Enter element\n")
    list.append(a)
for i in list[::-1]:
    print(i)

#Ques 2
string=input("Enter the string\n")
for i in string:
    if(i.isupper()):
        print(i)

#Ques 3
strng1=input("Enter value\n")
s=strng1.split(',')
lst=[]
for i in s:
    lst.append(int(i))
print(lst)


#Ques 4
st2=input("Enter string\n")
count=0
st1=st2[::-1]
if(st2==st1):
    print("The string is palindrome")
else:
    print("The string is not palindrome")

#Ques 5
import copy as c
list1=[1,2,4,[6,7],9,10]
list2=c.deepcopy(list1)
list1[3][0]=3
print(list1)
print(list2)
"""In deep copy the string is just copied to another string and if the
changes are made in 1st string then the second string is not affected
because it was copied bfore the changes were made"""

"""Where as in shallow copy reference object is copied to another string
so any changes made in string is directly implemented over the other string."""
