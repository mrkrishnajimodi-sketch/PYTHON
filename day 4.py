#operators
#airthmetic operators
#(+ , -, *,/ , //, %, **)
a = 20
b = 30
print(a + b)
print(a-b)
print(a*b)
print(int(a/b))
print(a//b) # it will remove the value after decimal point
print(a**b) # it is used for power operator
print(a%b) # it will find reminder

#take inputs of principle < rate and time and find out
#the simple interest (p*r*t/100)

P = int(input("please tell principle :"))
R = float(input("please tell rate :"))
T= int(input("please tell time:"))
ci = (P*R*T)/100
print(f"your simple interest is {ci}") 

#compound interest 

 
P = int(input("please tell principle :"))
R = float(input("please tell rate :"))
T= int(input("please tell time:"))
si = P*(1 + R/100**T)
print(f"copound interest is {si - P}")