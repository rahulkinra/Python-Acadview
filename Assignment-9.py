"""
Q.1- Name and handle the exception.
     a=3
     if a<4:
       a=a/(a-3)
       print(a)
"""
'''SOLUTION: This code will produce ZeroDivisionError.
             HANDLING THE EXCEPTION:                  '''
a=3
if a<4:
   try:
     a=a/(a-3)
   except ZeroDivisionError:
     print("Denominator can not be zero")

#Q.2- Name and handle the exception occurred in the following program: 
#      l=[1,2,3] 
#      print(l[3])

'''SOLUTION: The above code will throw the IndexError that means the index mentioned is out of range.
             HANDLING THE EXCEPTION:                                                                '''
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("The Index Mentioned above is out of range.")

"""
Q.3- What will be the output of the following code:
    try:
      raise NameError('Hi There')
    except NameError:
      print("An exception")
      raise
"""
'''SOLUTION: The output of the following code will be : 'An exception' followed by the error: 'NameError: Hi There' (displaying the msg)'''

"""Q.4- What will be the output of the following code: 
    Function which returns a/b
     def AbyB(a ,b):
       try:
           c = ((a+b) / (a-b))
       except ZeroDivisionError:
            print("a/b result in 0")
 
       else:
            print(c)
     Driver program to test above function
     AbyB(2.0, 3.0)
     AbyB(3.0, 3.0)
"""
'''OUTPUT:   -5.0
              a/b result is 0'''

# Q.5- Write a program to show and handle following exceptions: 
#       1. Import Error 
#       2. Value Error 
#       3. Index Error

'''  IMPORT ERROR:
     x=int(input("Enter the number: "))
     print(factorial(x))
     VALUE ERROR:
     x=int(input("Enter the number: "))
     print(X)
     INDEX ERROR:
     l=[1,2,3]
     print(l[3])
     HANDLING EXCEPTIONS:       '''

x=int(input("Enter the number: "))
try:
    print(math.factorial(x))
except:
    print("Import Error.")


try:
    x=int(input("Enter the number: "))
except ValueError:
    print("You entered the wrong type.")
else:
    print(x)


l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Index out of range.")
