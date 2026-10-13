"""arr=[10,20,30,40,50]
n=len(arr)
for i in range(0,len(arr)//2):
    arr[i],arr[n-i-1]= arr[n-i-1],arr[i]
print(arr)"""


"""l=[10,-5,20,-3,0,8]
print("positive")
for i in l:

    if i>0:
        print(i)

print("negative")
for i in l:
    if i<0:
        print(i)"""





"""l=[10,20,30,40,50,60]
sum=0
for i in l:
    sum=sum+i

print(f"mean--{sum/len(l)}")"""




l=[10,96,77,145,20]
max=l[0]
index=0
for i in range(1,len(l)):
    elem=l[i]

    if elem>max:
        max=elem
        index=i
        


print(f"max is {max} at index{index}")

