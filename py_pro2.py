import random

choices = ['rock', 'paper', 'scissors']

print("🎮 Rock, Paper, Scissors Game!")
print("Type rock, paper, or scissors. Type 'q' to quit.\n")

while True:
    user_choice = input("Your choice: ").lower()

    if user_choice == 'q':
        print("Game over. Thanks for playing!")
        break

    if user_choice not in choices:
        print("❌ Invalid input. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("😐 It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
