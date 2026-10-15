"""
DICTIONARY
1.ANNOATED BY{CURLY BRACES}
2. DICTIONARY IS COMBINATION MULTIPLE KEYS:VALUES
3.DICT ARE MUTABLE
4.DICT ARE HETROGENEOUS.
5.DICT ARE ORDER BECAUSE EVERY CHARCATER AHVE ITS UNIQUE KEY
6.IN DIC KEY WILL ALWAYS BE UNIQUE BUT VALUES CAN BE DUPLICATED
"""

# d={1:10,2:20,3:30}
# d[3]=100
# print(d)


# d={1:10,2:20,"krish":"sheryians","devraj":"MODI JI"}
# D={1:10,2:20,3:30,2:100}
# D[5]=90 #creating new key and assigning value
# print(D)


# d={1:10,2:20,3:30,4:40}
# for i in d:
#     print(i,d[i])




#method in dictionary

#to print or give oonly keys froom the dict.
#will give all the values from the dictionary.
#3.items()
#it will give both keys and value from the dictionary

# d={"a":1.0, "b":2.0,"c":3.0}
# print(d.keys)
# print(d.values)
# for key,value in d .items():#key:value
#     print(key,value)
#4.
d={"a":10,"b":20,"c":30}
d.pop("b")
print(d)