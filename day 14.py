#sum of digit
"""N=int(input("tell your number"))
sum=0
while N!=0:
   sum= sum+N%10
   N=N//10
print(sum)"""

#print the reverse of a number-123

#outut=321
""" N= int(input("tell me your number"))
rev=0
while N!=0:
   rev= rev*10+N%10
   N=N//10
print(rev)"""

#palindrome number

n= int(input("tell your number :"))

tem= n
rev=0
while n!=0:
     rev= rev*10+n%10
     print(rev)
     n=n//10
if  rev==tem:
     print("pallindrome")
else:
     print("not pallindrome")