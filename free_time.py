import random
import os

# ──────────────────────────────────────────────
#  SECTION 1: THE DECK
# ──────────────────────────────────────────────

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def build_deck():
    """Create a full 52-card deck and shuffle it."""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(rank + suit)
    random.shuffle(deck)
    return deck


def deal_card(deck):
    """Remove and return the top card from the deck."""
    return deck.pop()


# ──────────────────────────────────────────────
#  SECTION 2: SCORING
# ──────────────────────────────────────────────

def card_value(card):
    """Return the numeric value of a single card (Ace = 11 for now)."""
    rank = card[:-1]
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)


def calculate_score(hand):
    """Calculate the best score for a hand, flipping Aces from 11 to 1 if needed."""
    score = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[:-1] == "A")

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


# ──────────────────────────────────────────────
#  SECTION 3: DISPLAY
# ──────────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_hand(name, hand, hide_second_card=False):
    if hide_second_card:
        visible_cards = [hand[0], "??"]
        print(f"{name}'s hand: {' '.join(f'[{c}]' for c in visible_cards)}")
    else:
        score = calculate_score(hand)
        print(f"{name}'s hand: {' '.join(f'[{c}]' for c in hand)}  = {score}")


def display_table(player_hand, dealer_hand, hide_dealer=True):
    clear_screen()
    print("=" * 40)
    print("        ♠  BLACKJACK  ♠")
    print("=" * 40)
    display_hand("Dealer", dealer_hand, hide_second_card=hide_dealer)
    print()
    display_hand("You", player_hand)
    print()


# ──────────────────────────────────────────────
#  SECTION 4: GAME LOGIC
# ──────────────────────────────────────────────

def player_turn(player_hand, dealer_hand, deck):
    while True:
        display_table(player_hand, dealer_hand, hide_dealer=True)

        if calculate_score(player_hand) == 21:
            print("🎉 Blackjack! You have 21!")
            return True

        choice = input("(h)it or (s)tand? ").strip().lower()

        if choice == "h":
            player_hand.append(deal_card(deck))
            if calculate_score(player_hand) > 21:
                display_table(player_hand, dealer_hand, hide_dealer=True)
                print("💥 You busted!")
                return False

        elif choice == "s":
            return True

        else:
            print("Please enter 'h' or 's'.")


def dealer_turn(player_hand, dealer_hand, deck):
    display_table(player_hand, dealer_hand, hide_dealer=False)
    print("Dealer reveals their hand...")
    input("Press Enter to continue...")

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        display_table(player_hand, dealer_hand, hide_dealer=False)
        print("Dealer hits...")
        input("Press Enter to continue...")

    if calculate_score(dealer_hand) > 21:
        print("💥 Dealer busted!")
        return False
    return True


def determine_winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"\nYour score:   {player_score}")
    print(f"Dealer score: {dealer_score}")
    print()

    if player_score > dealer_score:
        print("🏆 You win!")
    elif dealer_score > player_score:
        print("😞 Dealer wins.")
    else:
        print("🤝 It's a tie!")


# ──────────────────────────────────────────────
#  SECTION 5: MAIN GAME LOOP
# ──────────────────────────────────────────────

def play_round():
    deck = build_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    player_safe = player_turn(player_hand, dealer_hand, deck)

    if player_safe:
        dealer_safe = dealer_turn(player_hand, dealer_hand, deck)
        display_table(player_hand, dealer_hand, hide_dealer=False)

        if not dealer_safe:
            print("🏆 Dealer busted — you win!")
        else:
            determine_winner(player_hand, dealer_hand)
    else:
        display_table(player_hand, dealer_hand, hide_dealer=False)
        print(f"\nYour score:   {calculate_score(player_hand)}")
        print("\n😞 Dealer wins.")


def main():
    print("Welcome to Blackjack!")
    input("Press Enter to start...")

    while True:
        play_round()
        print()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()