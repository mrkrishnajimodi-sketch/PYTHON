import random
#1-rock
#2-paper
#3- scissor
com_score=0
user_score=0
while True:
    print()
    print()

    if user_score==5:
        print("congrutulation you won")
        break
    elif com_score==5:
        print("sorry you loose")
        break
    print(f"score= computer{com_score} , human - {user_score}")
    com= random.randint(1,3)
    print("1- rock,2-paper,3-scissor")
    user= int(input("select your option:"))
    if user>=1 and user<=3:

        if user==com:
            print("its draw")
        elif user==1 and com==3:
            print('you won')
            user_score=user_score+1
        elif user ==2 and com==1:
            print("you won")
            user_score=user_score+1
        elif user ==3 and com==1:
            print("you won")
            user_score=user_score+1
        else :
            print('the computer won')
            com_score=com_score+1
    else:
        print('are you idiot')