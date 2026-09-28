#type conversion
#int(), float(), str(), bool()
# when you want to convert from one dta type to another you have to use type conversion
# int float and str are basic but if we talk about bool
# there are some falsse values -(0, 0.0 "",false,[] () {} none)
a = 12
b = 226.3
c = ""
d = 0
e = "56.2"
print(bool(a))
print(bool(b))
print(bool(""))
print(bool(d))
print(bool(e)) 
#inputs are simple but make sure to have the 
#righat data type while taking the inputs
name = input("what is your name  :")
age = input("what is your age :")
age = int(input("what is your age :"))
temp = float(input("what is the temp :"))
#input and output
#for providing the output you have only one thing and that is print()
"""print(harsh) kyu nhi hoga iska koi data type nahi hai hamesha dat type print hota hai"""
# how you can use variable while printing
name  = "anushka"
age = 21
# this is your first way
print ("hello how are you", name , "and your age is"  , age )
#2nd way is more simple
print(f"hello how are you { name } and your age is {age}")
           