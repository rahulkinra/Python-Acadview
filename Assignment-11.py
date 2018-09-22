

#Q.1- Write a python code to find a valid email address from a text.
#Ans:[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|icloud.com|rediffmail.com|hotmail.com)
import re
email = input("Enter email\n")
match = re.match('[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|icloud.com|rediffmail.com|hotmail.com)',email)
if match != None:
    print("Valid  email")
    parts = re.split('@',email)
    print("User name is ",parts[0]," Domain name is: ",parts[1])
else:
    print("Invalid Email")

#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits.)
#Ans:^(+91-)[6-9]\d{9}
phn = input("Enter a phone number\n")
#n = '+91-'+phn
m = re.match('^(\+91-)[6-9]\d{9}',phn)
if m != None:
    print("Valid phone number")
    numb = re.split('-',phn)
    print("Number is " , numb[1])
else:
    print("Invalid Phone number")
