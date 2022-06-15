#1

string=input("Type your string here: ")
my_string=''
for i in string:
    my_string=i+my_string
print(my_string)


#2

lower=int(input("Enter lower range limit : "))
upper=int(input("Enter upper range limit : "))
n=int(input("Enter the number to be divided by : "))
for i in range(lower,upper+1):
    if (i%n==0):
     print (i)


#3

import math
s1=float(input("Enter the side 1 : "))
s2=float(input("Enter the side 2 : "))
s3=float(input("Enter the side 3 : "))
if (s1+s2>s3 or s2+s3>s1 or s1+s3>s2) and s1>0 and s2>0 and s3>0:
    print("The combination exists")
else:
    print("Invalid Input")
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("The area of a traiangle is: ",round(area,2))


#4

n=5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


#5

#taking input for rows
rows=int(input("The number of rows to be printed: "))
n=0
for i in range(0,rows+1):
    for j in range(i):
            p=n//26 #we did this so that the pattern continue after Z
            #here chr(65) represents A
            print(chr(65+n-26*p), end="") 
            n+=1
    print("")


#6

lower=int(input("Enter the lowest range value : "))
upper=int(input("Enter the upper range value : "))
for number in range(lower,upper+1):
    if number>1:
        for i in range (2,number):
            if (number%i)==0:
                break
        else:
            print(number)

        
#7

for i in range(1,500):
    if (i%7==0) and (i%11==0):
        print(i)


#8

list = []
for i in range(10):
    z = int(input("Enter the number: "))
    list.append(z)
print("The negative numbers are: ")
for j in list:
    if j < 0:
        print(j)
print("The positive numbers are: ")
for j in list:
    if j > 0:
        print(j)
print("The odd numbers are: ")
for j in list:
    if j%2!=0:
        print(j)
print("The even numbers are: ")
for j in list:
    if j%2==0:
        print(j)
count = int(input("Enter the number to be counted: "))
count = list.count(count)
print("It occurs ", count," times")


#9

list_new = []
for i in range(10):
    z = input("Enter the word to be added in list: ")
    list_new.append(z)
word = input("Enter the word to be counted: ")
count_list = list_new.count(word)
print(word,"occurs",count_list,"times.")