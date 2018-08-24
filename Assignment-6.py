#Ques 1

def Sphere(radius):
    area=4/3 * 3.14 * (radius**2)
    return area
i=int(input("Enter the radius of the sphere"))
area=Sphere(i)
print(area)

#Ques 2

def perfect(number):
      sum=0
      for i in range(1,number):
            if number%i is 0:
                  sum=sum+i

      if sum == number:
            return number
      else:
            return 0


for i in range(1,1001):
      n=perfect(i)
      if n is not 0:
            print(n)


#Ques 3

num=int(input("enter the number"))
for i in range(1,11):
      print(i*num)

#Ques 4

def power(i,j):
    if j is 1:
        return i
    else :
      a= power(i,j-1)
      #print(a)
      return (i*a)
i=int(input("enter the number"))
j=int(input("enter the number"))
number=power(i,j)
print("i^j=",number)
