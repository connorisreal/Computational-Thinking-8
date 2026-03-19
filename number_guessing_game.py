import random
losses = 0
wins = 0

print("Welcome to the Number Guessing Game! You will have seven guesses to guess the number.")
print("\nLet's begin! Have fun!\n")

def playgame():
    global wins, losses
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100...")

    while True:
        guess = int(input("\nGuess the number: "))

        if guess < secret_number:
            print("Too low! Try again.\n")
            attempts += 1
        elif guess > secret_number:
            print("Too high! Try again.\n")
            attempts += 1
        else:
            print("\n🎉 You got it! Good job.\n")
            attempts += 1
            wins += 1
            break
        
        if attempts >= 7:
            print(f"Sorry, that's seven guesses. The number was {secret_number}. But good try!")
            losses += 1
            break
    if wins == 1:
        print(f"You have won {wins} game.")
    else:
        print(f"You have won {wins} games.")
    if losses == 1:
        print(f"You have lost {losses} game.")
    else:
        print(f"You have lost {losses} games.")

playgame()

while True:
    replay = input("Would you like to play again? (Y/N): ").upper()
    if replay == "Y":
        playgame()
    elif replay == "N":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("\nPlease enter 'Y' or 'N'.\n")