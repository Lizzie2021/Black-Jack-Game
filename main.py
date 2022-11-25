from art import logo
import random
import os


def black_jack_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer = {"cards": [], "score": 0}
    you = {"cards": [], "score": 0}

    def deal_card(player):
        card = cards[random.randint(0, 12)]
        if card == 11 and player["score"] > 10:
            player["cards"].append(1)
        else:
            player["cards"].append(card)
        player["score"] = sum(player["cards"])

    def show_results():
        print(f"Your final hand: {you['cards']}, final score: {you['score']}")
        print(f"Computer's final hand: {computer['cards']}, final score: {computer['score']}")
        if you['score'] > 21:
            print("You bust! :(")
        elif computer['score'] > 21:
            print("You win! :)")
        else:
            if you['score'] > computer['score']:
                print("You win! :)")
            elif you['score'] < computer['score']:
                print("You lose! :(")
            else:
                print("Draw!!!")

    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == "y":
        os.system("clear")
        print(logo)
        for _ in range(2):
            deal_card(you)
            deal_card(computer)
        while True:
            if you['score'] >= 21:
                show_results()
                break
            if computer['score'] >= 21:
                show_results()
                break
            print(f"Your card: {you['cards']}, current score: {you['score']}")
            print(f"Computer's first card: {computer['cards'][0]}")
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                deal_card(you)
            else:
                while computer['score'] < 17:
                    deal_card(computer)
                show_results()
                break
        black_jack_game()
    else:
        print("See you next time!")


black_jack_game()

