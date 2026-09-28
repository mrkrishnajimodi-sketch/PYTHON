"""N=int(input("tell your number"))
count=0
for i in range(1, N+1):
    if i%3==0 and i%5==0 :
        count=count +1
print(count)"""

"""N= int(input("tell your number"))
count=0
for i in range(1 ,N):
    if i%N==0:
        count=count+1

if count==2:
    print("the number is prime")
else:
    print("the number is composite")"""


"""a=int(input("tell your number"))
B= int(input("tell your second number"))
if a>B:
        for i in range(a,0,-1):
            if B%i==0 and a%i==0:
                print(f"hcf-{i}")
                break
if B>a:
     for i in range(a,0,-1):
          if B%i==0 and a%i==0:
               print(f"hcf-{i}")
               break
else :
     print(f"hcf-{a}")"""



A= int(input("tell your number"))
count=0
while A>0:
    if (A%10):
        count=count+1
        A=A//10
print(count)






    
