#list methods
""" l=[10,20,30]
l.append(40)"""

"""a=[10,20,30,40]
b=a.copy()
b[0]= 1000#shallow copy
print(a)
print(b)"""


"""a=[1,2,3,1,2,31,1,2,2,1]
a.extend([10,20,30])
print(a.extend)"""

"""a=[10,20,30]
popped=a.pop(1)
print(a)
print(popped)
a.remove(20)
print(a)"""#from left to right the first occurance number willl removed

"""a=[10,20,30,96,75,879,52678]
a.sort(reverse=True)
print(a)"""



"""a=[10,20,30,40,50]
b=[]
for i  in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)"""

"""a=[10,20,30,40,50,60,70]
temp=len(a)-1
for i in range(0,(len(a)-1)//2):
    a[i],a[temp]=a[temp],a[i]
    temp=temp-1
print(a)"""


    


