"""N = int(input("tell your number"))
sum=0
temp=N
while N!=0:
    Z=N%10
    fact=1
    
    for i in range(1,Z+1):
        fact=fact*i
    sum=sum+fact
    print(sum)


    N=N//10

if sum==temp:
    print("strong number")
else:
    print("not strong number")"""


 #number guessing gamen 

import random
num=random.randint(1,100)
tries=0
while True:
    tries= tries+1
    guess= int(input("guess your numbe btw 1-100"))
    if guess==num:
        print("congrutulation you won in tries ", tries)  
        break
    elif guess>num:
        print("go a bit lower")
    else:
        print("go a bit higher")