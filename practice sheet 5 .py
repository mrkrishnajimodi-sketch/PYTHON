"""Age = int(input("tell your age"))
if Age >= 18 :
    print("eligible for  lincense")
else :
    print("not eligible for license")
learnerLicense = input("yes or no")
if learnerLicense == "yes":
    print("yes")
else : 
    print("no")
DrivingtestPasssed=input("driving test  paseed :")
if DrivingtestPasssed == "yes":
    print("license approved")
else :

    print("lincense not approved")"""














plan = input("tell your internet plan : ")

if plan == "premium" :
    usage=int(input("tell me how much data you used "))
    if usage<=300:
        auto_renewal=input("tell me if you want autorenewal or not ")
        if auto_renewal=="yes":
            print("799 plan")
        else:
            print("849")
    else:
        print("limit gone ")

elif plan=="basic":
    usage=int(input("tell me how much data you used "))
    if (usage<=100):
         print("price : 499")
    else:
         auto_renewal=input("tell me if you want autorenewal or not ")
         if auto_renewal=="yes":
                     print("599 plan")
         else:
                     print("premium")
else:
     print("bhai basic ya premium hi le sskte ho bas")


#mujhe isko hi print krana h agr mein plan type likhu premium toh mujhe premium hi print chahiye only aghr basic lkhu toh mujhe basic chaihoye 


# if starting mein likh diya meine but else ki condition nhi work krti agr meinb nestef if laha deta  hu
if plan == " basic":
    if plan ==" premium" :
        print("pla is premium")
    else :
        print("plan is not oremium")
else :
    plan == "basic plan"










"""per = int(input("tell me your percentage"))
FamilyIncome = int(input("tell me your family income"))
sportsAchievements  = input("any sports achievemets : ")

if per >= 80 :
    if FamilyIncome <= 300000 :
        print("you will get full scholarship")
    elif sportsAchievements  == "yes" :
        print("you will get partial schorlarship")

    else :
        print("you will no get any scholarship")
    if per >=60 and per <=79 :
        if sportsAchievements =="yes":
            print("you will get sports schorlarships :")
        else :
            print("you are not eligible")"""




    
