#find even factor counter
"""N=int(input("tell your number"))
count=0
for i in range(1,N+1):
    if N%i==0 and i%2==0:
        count=count+1
print(count)"""

#Largest proper factor
"""N=int(input("tell your number"))
count=0
for i in range(N//2+1, 1,-1):   #mistake  thi ssteps likhna hi bhhool gya tha
    if N%i==0:
        count=count+i
        break         #condition prove hone ke baad baaki sari iteratipon ko rok dega
print(count)"""


#sum of factor

"""N= int(input("tel your number"))
count=0
for i in range(1,N+1):
    if N%i==0:
        count=count+i
        print(count)"""

#count number with exactly 3 factor

"""N=int(input("tell your number"))
count=0
for i in range(1,N+1):
        factor=0

for J in range(1,i+1):
        if i%J==0:
               factor=factor+1     # isss question o smjhana ya video solution dekho best tarika     
if factor==3:
        count=count+1
        print(i)
print(count)"""





"noof digit question in for loop"

"""N = int(input("Enter your number: "))
count = 0

for i in range(N):   # loop N times chalega, but break karenge jab N khatam ho
    if N == 0:
        break
    count += 1
    N = N // 10"""

"""print("Number of digits:", count)"""
"""N= int(input("tell your number"))
count=0
while N!=0:
    count=count+1
    N=N//10
print(count)"""

N= int(input("tell me your number"))
