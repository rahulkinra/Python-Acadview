#Ques 1
abc=eval(input('enter the dictionary'))
xyz=int(input('enter the value in the dictionary'))
for l,m in abc.items():
    if xyz==m:
        break
print(l)

#Ques 2
Dict={'Ronaldo':{'Maths':45,'Spanish':60,'Punjabi':99},'Albert':\
         {'Maths':72,'Sanskrit':100,'French':85},'Newton':\
         {'Maths':95,'Spanish':82,'Punjabi':60}}
value=input("Enter the name of student : ")
for i in Dict:
    if value==i:
        print(i,Dict[i])
