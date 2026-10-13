'''A=int(input("tell your number"))
sum=0
while A!=0:
    Z=(A%10)
    sum= sum+Z
    A=A//10
print(sum)'''


"""N= int(input("tell your number"))
rev=0

while N!=0:
    Z= N%10
    rev= rev*10+Z
    N=N//10
print(rev)"""


"""N= int(input("tell your number"))
rev=0
tem=N
while N!=0:
    Z=N%10
    rev= rev*10+Z
    N=N//10
print(rev)
if rev==tem:
    print("the number is pallindrome")
else:
    print("the number is not pallindrome")"""




#mnested loop question

N=int(input("tell your number"))
sum=0


while N!=0:
    Z=N%10
    fact=1

    for i in range (1, Z+1):
        
        fact=fact*i
        sum=sum+fact

    
print(sum)











