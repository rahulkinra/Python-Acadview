#ques 1
class circle():
    def __init__(self,r):
        self.rad=r
    def getArea(self):
        return 3.14*self.rad*self.rad
    def getCircumference(self):
        return 2*3.14*self.rad

r=int(input("Enter radius\n"))
ob=circle(r)
print("Area is ",ob.getArea())
print("Circumference is ", ob.getCircumference())

ques 2
class student():
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def display(self):
        print("Name of student is ",self.name,"and his roll no is",self.roll,"he is",self.age,"Years old and having",self.marks,"Marks")
    def getMarks(self,m):
        self.marks=m
    def getAge(self,a):
        self.age=a
n=input("Enter name of student\n")
r=int(input("Enter roll no of student\n"))
marks=int(input("Enter marks\n"))
age=int(input("Enter age\n"))
ob=student(n,r)
ob.getAge(age)
ob.getMarks(marks)
ob.display()
ques 3
class temprature():
    def convertFahrenheit(self,cel):
        self.cel=cel
        far=(self.cel*9/5)+32
        print(far)
    def convertCelsius(self,farh):
        self.farh=farh
        cel=(self.farh-32)*5/9
        print(cel)
n=int(input("Convert to\n 1.farhenheit \n 2.celsius\n"))
ob=temprature()
if(n==1):
    x=float(input("Enter celsius\n"))
    ob.convertFahrenheit(x)
else:
    x=float(input("Enter farhenheit\n"))
    ob.convertCelsius(x)

ques 4
class movie():
    def __init__(self):
        self.artist='NA'
        self.year='NA'
        self.rating='NA'
    def add(self,a,y,r):
        self.artist=a
        self.year=y
        self.rating=r
    def display(self):
        print("artist: ",self.artist,"Year of release: ",self.year,"Ratings: ",self.rating)
n=input("Do you want to add detais? Y:N")
ob=movie()
if(n=='y'):
    a=input("Enter artist name")
    b=int(input("Enter year"))
    c=int(input("Enter ratings"))
    ob.add(a,b,c)
else:
    ob.display()

#ques 5
class animal():
    def animal_attribute(self):
        print("Class animal")
class tiger(animal):
    pass
ob=tiger()
ob.animal_attribute()
# ques 6
"""
the output of code will generate error as the print statement doesnt have proper brackets but except that it will generate:
A B
A B
"""

# ques 7
class shape():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area is ",self.l*self.b)
class square(shape):
    pass
class rectangle(shape):
    pass
l=int(input("Enter length\n"))
b=int(input("Enter breadth \n"))
if(l==b):
    obj=square(l,b)
    obj.area( )
else:
    obj=rectangle(l,b)
obj.area( )
