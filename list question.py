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








"""l=[1,2,4,5]
n=(len(l))
original=n+1
original_sum=0
# original_sum=original*original+1//2
for i in range(1,original+1):
    original_sum=original_sum+1
real_sum=0    
for elem in l:
    real_sum+=elem

missing=original_sum-real_sum

print(missing)"""





"""l=[10,20,30,40,50,60]
sum=0
for i in l:
    sum=sum+i

print(f"mean--{sum/len(l)}")"""




"""l=[10,96,77,145,20]
max=l[0]
index=0
for i in range(1,len(l)):
    elem=l[i]

    if elem>max:
        max=elem
        index=i

print(f"max is {max} at index{index}")"""




# l=[10,20,40,50]
# is_sorted=True

# for i in range(1,len(l)-1):

#     if (l[i]>l[i+1]):
#         is_sorted=False
#         break

# if is_sorted:
#         print("list is  sorted")

# else:
#      print("list is not sorted")

# l=[2,3,15,15,3,2]
# n=len(l)
# is_pallindroome=True
# for i in range(n//2):
#     if l[i]!=l[n-i-1]:
#         is_pallindroome=False
#         break
# if is_pallindroome:
#     print("list is pallindrome")
# else:
#     print("not in pallindrome")





# ----sorting of list
# #bubble sort question
# l=[64,34,25,12,22,11,]
# n=len(l)
# for i in range(n):
#     for j in range(n-1-i):#n-1 we can use it allso
  
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[i]

# print(l)




"""l=[10,20,40,90,50]
l.sort(reverse=True)
print(l)"""



