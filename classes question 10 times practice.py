#print range fxn
"""for i in range(5) :
    print(i)
for i in range(1 ,5):
    print(i)
for i in range(-32, 42 , 1) :
    print(i)"""
"""for i in range(42 , -32 , -1) :
    print(i)"""
"""for i in range(200,400, 36) :
    print(i)"""

#write a table
"""for i in range(7 , 7*10 +1 , 7) :
    print(i)
for i in range(9 ,9*10+1 , 9):
    print(i)
N= int(input("tell your which table hav eto print"))
for  i in range (N , N*10 +1 , N) :
    print(i)"""
"""N= int(input(" tell yournumber"))
for i in range (N , N*10, N):
    print(i)"""
"""N= int(input("tell your number "))
for i in range (1 , 11):
    print(f"{N} *{i}={N*i}")"""





#print the sum of natural number from one to n
"""N= int(input(" tell your number"))
sum =   0
for i in range ( 1 , N+1) :
    sum = sum +i
print(sum)"""

#summary of question  = python hamesha input ko text ya string ke roop mein leta h i
#tabhi apna int ka use krte h uska intger mein convert krne ke liye

"""N= int (input(" telll your number"))
sub = 0
for i in range (6, -1 , -1) :
    sub= sub-i
print(sub)"""


"""N= int(input("tell your number"))
fact= 1
for i in range (1 , N+1):
    fact= fact*i
print(fact)"""

"""N= int(input("tell your number"))
factor = 0
for i in range(1 , N+1):
    if N%i==0 :
        factor =  i
        print(factor)"""




"""N= int(input("tell your number"))
count = 0
for i in range (1,N+1) :
    if N%i==0:
        count= count+1
count==2
if count==2 :
    print ("number is prime")
else :
    print("number is not prime")"""


#2nd method for prime number

N= int(input(" tell your number"))
count= 0
for i in range (2 ,N//2 +1) :
    if N%i==0:
        print("number is composite")
        break
else :
    print("number is prime")