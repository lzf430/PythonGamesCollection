from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    '''Check the answer against guess, and return the turns remaining'''
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You are right! The number was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Hard or Easy: ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def game():
    print(logo)

    print("Welcome to Guessing Game!")
    print("I am thinking a number between 1 and 100.")
    answer = random.randint(1, 101)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have ran out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again!")


game()