import random
user_score=0
computer_score=0
values=("r", "p", "s")
while True:
    if user_score == 3 or computer_score == 3:
        break
    user_choice=input("Choose rock (r), paper (p) or scissors (s): ")
    if user_choice.lower()!="r" and user_choice.lower()!="p" and user_choice.lower()!="s":
        print("Choose again properly")
    else:
        computer_choice=values[random.randint(0,2)]
        print(f"Computer choice: {computer_choice}")
        if user_choice==computer_choice:
            print(f"It's draw. Your score: {user_score} Computer score: {computer_score}")
        elif (user_choice=="r" and computer_choice=="s") or (user_choice=="s" and computer_choice=="p") or (user_choice=="p" and computer_choice=="r"):
            user_score += 1
            print(f"You won. Your score: {user_score} Computer score: {computer_score}")
        else:
            computer_score += 1
            print(f"Computer won. Your score: {user_score} Computer score: {computer_score}")
if user_score==3:
    print("You won the whole game")
else:
    print("You lost the whole game")