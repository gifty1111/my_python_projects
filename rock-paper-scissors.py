import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
computer_choice = random.randint(0,2)
print(f"Computer choose: {computer_choice}")

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number. You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == computer_choice:
    print("it's a draw")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")


