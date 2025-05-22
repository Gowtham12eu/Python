import random as rd
user_wins=0
computer_wins=0 
operation=["stone","paper","scissors"]

while True:
    type=input("Type Stone/Paper/scissors or Q to quite:").lower()

    if type=="q":
      break

    if type not in  operation:
       continue

    ra=rd.randint(0,2)
    computer_picks=operation[ra]
    print("computer picks:" + computer_picks +  ".")

    if type=="stone" and computer_picks=="scissors":
       print("You won")
       user_wins+=1

    elif type=="paper" and computer_picks=="stone":
       print("You win")
       user_wins+=1

    elif type=="scissors" and computer_picks=="paper":
       print("you win")
       user_wins+=1
    
    elif type==computer_picks:
       print("TIE")
       
    else:
       computer_wins+=1
       print("lost")

print("user:" , user_wins)
print("computer:" , computer_wins)


