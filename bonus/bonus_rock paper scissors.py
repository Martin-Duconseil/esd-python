import random

def play_game():
    # Define the options
    options = ["rock", "paper", "scissors"]

    # Get the user's choice
    user_choice = input("Choose rock, paper, or scissors: ")

    # Check if user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Print the choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()
