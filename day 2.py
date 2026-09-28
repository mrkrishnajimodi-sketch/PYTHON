#string 
"""every thong inside a string has a unique code and to find out  
you have ro find that you have to use ord()
"""
name = "virat kohli"
print(ord("v")) # you can see the v have its unique code 118
"""from A to Z the unique code is 65 to 90 
 and for small a to z the unicode is start 97 to 122"""

# indexing
"""every element insie your string can be accesed using index
there are two types of index one is positive string start from 0 and its goes from left to right 
and second is negative start from -1it goes right to left"""
#reminder - space are also used in  index and count 
s = "anushka sahu"
print(s[6]) # this is called positive indexing
print(s[-4]) # this is called negative inndexing 

#slicing 
"""in slicing there are  three s first s start , stop , step"""
a = "muskan sahu"
print(a[0:6:1])
print (a[ : : ])