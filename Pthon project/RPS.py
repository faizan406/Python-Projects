import random

item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your move=Rock,Paper,Scissor=")
computer_choice=random.choice(item_list)

print(f"User Choice={user_choice}, Computer Choice ={computer_choice}")

if user_choice==computer_choice:
    print("Both choices same: =Match Tie")
    
elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper covers Rock =computer win")
    else:
        print("Rock smashes scissor=YOU WON")

elif user_choice=="Paper":
    if computer_choice=="Rock":
        print("Paper Cover Rock=YOU WON")
    else:
        print("Scissor Cuts Paper=Computer Won")

elif user_choice=="Scissor":
    if computer_choice=="Paper":
        print("Scissor Cuts a Paper=You WON")
    else:
        print("Rock Smahes Scissor=Computer won")