import random
from higherart import logo, vs
from higherdata import data


def selection(data):
    return random.choice(data)


def format_output(choice):
    choice_name = choice['name']
    choice_description = choice['description']
    choice_country = choice['country']
    return f"{choice_name}, {choice_description}, {choice_country}"


def checking(guess, choice_a, choice_b):
    return (guess == "a" and choice_a['follower_count'] > choice_b['follower_count']) or (guess == 'b' and choice_b['follower_count'] > choice_a['follower_count'])


def game():
    print(logo)
    print("Welcome to Higher or Lower Game!")
    print("Guess the one with higher Instagram Followers!")
    score = 0
    choice_a = selection(data)
    choice_b = selection(data)

    while True:
        choice_a = choice_b
        choice_b = selection(data)

        while choice_a == choice_b:
            choice_b = selection(data)

        print(f"Compare A: {format_output(choice_a)}.\n")
        print(vs)
        print(f"B: {format_output(choice_b)}\n")
        guess = input("Which account has higher followers: A or B? ").lower()
        is_check = checking(guess, choice_a, choice_b)
        if is_check:
            score += 1
            print(f"You are right. Current score: {score}")
        else:
            print(f"Sorry, you are wrong. Final score: {score}")
            break


game()