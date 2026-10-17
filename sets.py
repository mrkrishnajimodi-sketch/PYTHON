#sets
#1. sets are annoted by curly bracket or set()
#empty curly bracket dictionary or , seperated values aa jati h then sets
#2. sets are collection of unique items
#3 sets are hetrogeneous
#4 sets are unordered because sets does not have indexing
#as sets dont have indexing we can not replace anyvalue its immutable

# s={1,2,3,4,5}
# print(type(s))

# s1={1,2,3,4,5,True,80.2,"sample"}
# #s2=set()
# print(s1)#true=0,False =3

# l=[1,1,2,2,3,3,4,4,5]
# print(set(l))

""""METHODS OF SET"""


# S={1,1,2,3}
# #add-- to add any element inside of set
# S.add(4)
# print(S)
# #..remove()--. remove any element from set
# S.remove(3)
# print(S)
# #..discard()--> if element not prsesent inside the set it will not so any error
# S.discard(6)
# print(S)




"""OPERATION

1.UNION--> MERGE BOTH THE STES
2. INTERSECTION-->COMMON ELEMENTS
3. difference--. ese element jo ek set but dusre mai nahi
4.SYMMETRIC DIFFERENCE---IT REMOVE THE COMMON ELEMENT
5.S1|s2 this is the operator for union
6.S1&S2 THIS IS THE OPERATOR FOR INTERSECTION 
7. S1-S2 FOR DIFFERENCE
8. S1^S2 SYMMETRIC KE LIYE """
# S1={1,2,3,4,5,6}
# S2={7,8,9,10,11}
# print(S1.union(S2))
# print(S1. intersection(S2))
# print(S1.difference(S2))
# print(S2.difference(S1))
# print(S1.symmetric_difference(S2))







# S={1,2,3,4,5}
#     S.add(6)
#     print(S)

# s=frozenset([1,2,3,4,5])
#     s.add(6)
#     s.remove(4)
#     print(s)

