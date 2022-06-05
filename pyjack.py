import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

total_wins = 0
total_losses = 0
hand_count = 0

def scoreboard():
    print("Wins: " + str(total_wins))
    print("Losses: " + str(total_losses))

def deal(deck):
	hand = []
	for i in range(2):
		random.shuffle(deck)
		card = deck.pop()
		if card == 11:
			card = "J"
		if card == 12:
			card = "Q"
		if card == 13:
			card = "K"
		if card == 14:
			card = "A"
		hand.append(card)
	return hand


def play_again():
    scoreboard()
    again = input("Do you want to play again? (Y/N): ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        scoreboard()
        game()
    else:
        print("Bye!")
        exit()


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return hand

def print_results(dealer_hand, player_hand):
    clear()
    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()


def score(dealer_hand, player_hand):
    global total_wins
    global total_losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Blackjack! You win this round!\n")
        total_wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("The dealer got a blackjack. You lose this round!\n")
        total_losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Bust! you lose!\n")
        total_losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Dealer busts. You win!\n")
        total_wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("You lose! Dealer has the higher score\n")
        total_losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("You win this round with a higher score!\n")
        total_wins += 1


def game():
    choice = 0
    clear()
    print ("WELCOME TO BLACKJACK!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print("The dealer is showing a " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input(
            "Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == "h":
            hit(player_hand)
            if total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print ("Bye!")
            exit()


if __name__ == "__main__":
    game()
