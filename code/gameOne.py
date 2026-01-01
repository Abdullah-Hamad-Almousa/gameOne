import random
import sys

choices = ["rock", "paper", "scissors"]

print("Welcome to the Rock-Paper-Scissors Game!")
print("Instructions: Enter rock, paper, or scissors.\n")
# Main code ^^^
while True:
    try:
        user_choice = input("Enter Your Choice: ").lower().strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting Game.")
        sys.exit()

    if user_choice in choices:
        break
    print("Invalid Choice. Please Try Again.")

computer_choice = random.choice(choices)

print(f"Computer Chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a Tie!")
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
     (user_choice == 'Paper' and computer_choice == 'Rock') or \
     (user_choice == 'Scissors' and computer_choice == 'Paper'):
    print("You Win!")
else:
    print("Computer Wins!")