import random

def deal_card():
    """Deal 2 cards from cards_list"""
    cards_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 , 10]
    card = random.choice(cards_list)
    return card


def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)
        print(f"   Your cards: {user_cards}, Current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score == 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'Y' to get another card, type 'N' to pass.\n").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_cards(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower() == "y":
  play_game()