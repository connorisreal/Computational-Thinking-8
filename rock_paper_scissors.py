import random
choices = ["rock", "paper", "scissors"]

print("\nHello there! Today we're playing rock, paper, scissors!")
print("\nLet's begin. Whoo!")

def playagain():
    playerchoice = input("\nChoose: Rock, Paper, or Scissors: ").lower()

    while playerchoice not in choices:
        playerchoice = input("\nInvalid choice. Please choose rock, paper, or scissors: ").lower()
    
    computerchoice = random.choice(choices)

    print("                                  |")
    print("                                  |")
    print(f"       Computer chose: {computerchoice:<10} |      Player chose: {playerchoice}")
    print("                                  |")
    print("                                  |")

    if playerchoice == computerchoice:
        print("\nIt's a tie!\n")
    elif (playerchoice == "rock" and computerchoice == "scissors") or (playerchoice == "scissors" and computerchoice == "paper") or (playerchoice == "paper" and computerchoice == "rock"):
       print("You win! Good job.")
    else:
       print("Computer wins!")

    replay = input("Play again? (Y/N): ")
    if replay.lower() == "y":
        playagain()
    else:
        print("Ok. Good game!")
playagain()