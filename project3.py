from utils import *
money = 1000

# Section 1 - Variables
# TODO - add starting values for all the variables
def play_game():
    global money
    turtle.clearscreen()

    x1 = -300
    y1 = -20
    x2 = -300
    y2 = 160
    x3 = -300
    y3 = 75
    x4 = -300
    y4 = -110


    # Section 2 - Setup
    set_background("racetrack_4")
    t1 = create_sprite("horse_racer_red_scale",x1,y1)
    t2 = create_sprite("horse_racer_green_scale",x2,y2)
    t3 = create_sprite("horse_racer_orange_scale",x3,y3)
    t4 = create_sprite("horse_racer_blue_scale",x4,y4)

    print(f"You have: {money} dollars.")
    bet = int(input("\nInput betting amount: "))
    if bet > money:
        while True:
            bet = int(input("\nBet exceeds maximum money. Please input bet: "))
            if bet <= money:
                break
    print("\nR = Red, G = Green, B = Blue, O = Orange\n")
    horse_bet = input("Which horse will you bet on (R, G, B, O): ").lower()
    if horse_bet not in ["r", "g", "b", "o"]:
        while True:
            horse_bet = input("\nInvalid choice. Choose R, G, B, or O: ")
            if horse_bet in ["r", "g", "b",  "o"]:
                break



    # # Section 3 - Racing
    # All sprites have a random speed with the same range, meaning it is completely random who wins 
    game_over = False

    time.sleep(3)

    while not game_over:
        x1 += random.randint(7, 20)
        x2 += random.randint(7, 20)
        x3 += random.randint(7, 20)
        x4 += random.randint(7, 20)

        t1.goto(x1, y1)
        t2.goto(x2, y2)
        t3.goto(x3, y3)
        t4.goto(x4, y4)

        window.update()
        time.sleep(0.1)
    
        if x1 > 280:
            print("Red horse wins!")
            if horse_bet == "r":
                money += bet
                print("\nYour bet was correct!")
            else:
                money -= bet
                print("\nSorry, your bet was incorrect.")
            game_over = True
        elif x2 > 280:
            print("Green horse wins!")
            if horse_bet == "g":
                money += bet
                print("\nYour bet was correct!")
            else:
                money -= bet
                print("\nSorry, your bet was incorrect.")
            game_over = True
        elif x3 > 280:
            print("\nOrange horse wins!")
            if horse_bet == "o":
                money += bet
                print("\nYour bet was correct!")
            else:
                money -= bet
                print("\nSorry, your bet was incorrect.")
            game_over = True
        elif x4 > 280:
            print("Blue horse wins!")
            if horse_bet == "b":
                money += bet
                print("\nYour bet was correct!")
            else:
                money -= bet
                print("\nSorry, your bet was incorrect.")
            game_over = True

    if money < 1:
        print("\nSorry, but you are broke. You lose.")
    else:
        while True:
            replay = input("\nWould you like to play again? (Y/N): ").lower()
            if replay == "y":
                play_game()
                break
            elif replay == "n":
                print("\nOk. Thanks for playing!")
                break
            else:
               print("\nInvalid answer. Please choose Y or N.")

play_game()
turtle.exitonclick()