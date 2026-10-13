"""for i in range(5):
    for j in range(5):
        print("*", end=(""))
    print()"""



"""l=4
b=3
for i in range(l):
    for j in range(b):
        print("*",end=(""))
    print()"""


"""N=5
for i in range(1,N+1):
    for j in range(1,N-i+1+1):
        print("*", end=(" "))

    print()"""




N=5
for i in range(1,N+1):
    for k in range(1,N-i+1+1):
        print(" " , end="")
    for j in range(i):
        print("*", end=(" "))

    print()



"""N=5
for i in range(1,N+1):
    for j in range(N):
        print("-",end=(""))
    for k in range(N):
        print("*", end="")
    print()"""
