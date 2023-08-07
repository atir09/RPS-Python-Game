import random
import os

def main():
    user_score=0
    computer_score=0
    draws=0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors), or 'quit' to exit: ").lower()

        if user_choice == 'quit':
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if user_choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        print(f"Draws: {draws}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        os.system('cls')

if __name__ == "__main__":
    main()