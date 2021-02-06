import random
import art

def deal_card():
    """ Returns A Random Card From The Deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Take List Of Cards And Returns The Calculated Score From Cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose, Opponent Has BlackJack."
    elif user_score == 0:
        return "Win With BlackJack."
    elif user_score > 21:
        return "You Went Over. You Lose."
    elif computer_score > 21:
        return "Opponent Went Over. You Win."
    elif user_score > computer_score:
        return "You Win."
    else:
        return "You Lose"

def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' To Get Another Card, Type 'n' To Pass : \n")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}.")
    print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}.")
    print(compare(user_score, computer_score))

while input("Do You Want To Play Game Of Black Jack ? Type 'y' Or 'n'") == "y":
    play_game()