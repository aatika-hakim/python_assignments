import random

# Const
ROUNDS = 5

def play_game():
    # Introduction
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_number in range(1, ROUNDS + 1):
        # Generate random numbers
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Display the round and player's number
        print(f"Round {round_number}")
        print(f"Your number is {player_number}")

        # Get player's guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Ensure the input is valid
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower': ")
            guess = input().strip().lower()

        # Check if the player's guess is correct
        if (guess == "higher" and player_number > computer_number) or \
            (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Print the score after each round
        print(f"Your score is now {score}\n")

    # Print the final result based on the score
    print(f"Your final score is {score}")

    if score == ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

play_game()
