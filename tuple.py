#tuple;

# a tuple is an ordered , immutable collection .
"""once you create it , you can not change ,add or remove items """
"""1. ANNOTED BY PARENTHESIS () 
2. ordered
3. tuple are hetrogeneous
4. duplicate elements are allowed
5. tuple is immutable completely
6. we  can do slicing also in tuple"""

#methods  of tpuple
#1..count--> count the occurance of any value
t=(1,1,2,3,4,1,2,4,1)
print(t.count(1))

#2.. INDEX()--> SHOW THE INDEX LOCATION OF THE FIRST OCCURING ELEMENT.
T=(1,2,1,2,1)
print(t.index(2))



#operation
t1=(1,2)
t2=(3,4)
print(t1+t2)
print(t1*5)

T=()# empty tuple
print(type(T))



T=(1,2,[2,3,4])

T[2].append(100)
print(T)
