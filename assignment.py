
print(' **********************')
print(' Assignment 0 ')
print(' **********************','\n')

print("Hello World")

print(' **********************')
print(' Assignment 1-1 ')
print(' **********************','\n')

k=[]
a = int(input('Insert a Number: '))
k.append(a)
while True:
    if  a!='exit':
        b = input('Insert a Number or \"exit": ')
        if b!='exit':
         k.append(int(b))
         print(sum(k))

        else:
            print('Good Bye')
            break


print(' **********************')
print(' Assignment 1-2 ')
print(' **********************','\n')

a=input('Insert time in acceptable format(00:00:00): ')
k=[]
for i in a:
    k.append(i)

print(k)

print((int(k[0]+k[1])*3600)+int(k[3]+k[4])*60+int(k[6]+k[7]))


print(' **********************')
print(' Assignment 1-3 ')
print(' **********************','\n')

a=int(input('Insert time in seconds: '))

print(str(int(a/3600))+':'+str(a%60-a%3600)+':'+str(a%3600))

print(' **********************')
print(' Assignment 1-4 ')
print(' **********************','\n')

aa=input('Number of Students: ')
import numpy as np

scorelist=[]

for i in range(int(aa)):

    score=input('remark student'+str(i)+': ')
    scorelist.append(score)

scorelist1=[int(i) for i in scorelist]

print('maximum of scores is:'+str(max(scorelist)))
print('minimum of scores is:'+str(min(scorelist)))
print('average of scores is:'+str(int(sum(scorelist1)/len(scorelist1))))


print(' **********************')
print(' Assignment 1-5 ')
print(' **********************','\n')

import random
a=random.randint(1,6)
print(a)
while a==6:
 b=random.randint(1,6)
 print(b)


print(' **********************')
print(' Assignment 1-6 ')
print(' **********************','\n')


terms = int(input("Insert a Number: "))

n1, n2 = 0, 1
count = 0


if terms <= 0:
   print("Please enter a positive integer")

elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < terms+1 :
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

print(' **********************')
print(' Assignment 1-7 ')
print(' **********************','\n')

print(' **********************')
print(' Assignment 1-8 ')
print(' **********************','\n')

a = float(input('Insert length of the first side: '))
b = float(input('Insert length of the second side: '))
c = float(input('Insert length of the third side: '))

if ((a+b) >c) and ((a+c) >b) and ((b+c) >a):
    print('Triangle can be drawn!')
else:
    print('Triangle can not be drawn!')


print(' **********************')
print(' Assignment 1-9 ')
print(' **********************','\n')

weight = float(input('Insert your weight in (kg): '))
height= float(input('Insert length your height in (m): '))

bmi=weight/(height**2)

if bmi <18.5:
    print('Your are underweight')

elif bmi >18.5 and bmi<24.9 :
    print('Your are normal')

elif bmi >25 and bmi<29.9 :
    print('Your are overweight')

elif bmi >30 and bmi<34.9 :
    print('Your are obese')

else:
    print('Your are extremely obese')



print(' **********************')
print(' Assignment 1-10 ')
print(' **********************','\n')

name = input('Insert your name: ')
score1= float(input('Insert the first score: '))
score2= float(input('Insert the second score: '))
score3= float(input('Insert the third score: '))

average=(score1+score2+score3)/3

if average >17:
    print(name+'!'+' You are great')

elif average >=12 and average<17:
    print(name+'!'+' You are normal')

else:
    print(name+'!'+' You are failed')


