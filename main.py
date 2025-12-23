import random
print("==Rock Paper Scissors Game==")
choices=["rock","paper","scissors"]
user_score=0
computer_score=0
while True:
    print("Choose:rock,paper,scissors or type exit to quit the game")
    user_choice=input("Enter your choice:").lower()#convert choice into lowercase to avoid errors.
    if user_choice=="exit":
        print("Game Over!!!")
        break
    if user_choice not in choices:
        print("Invalid Choice.Try again Later....")
        continue
    computer_choice=random.choice(choices)
    print("Computer Choosed:",computer_choice)
    if user_choice==computer_choice:
        print("It's a tie.")
    elif (user_choice=="rock" and computer_choice=="scissors" or user_choice=="paper" and computer_choice=="rock" or user_choice=="scissors" and computer_choice=="paper"):
        print("You win this round.")
        user_score+=1
    else:
        print("Computer win this round.") 
        computer_score+=1
    print(f"Your current Score:{user_score}\nComputer's current Score:{computer_score}")
print(f"Your final score:{user_score}\nComputer's Final Score:{computer_score}")
print("Thankyou for Playing game!!!")
