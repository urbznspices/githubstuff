
import random


def generate_word():
    word_list = ["apple", "banana", "cherry", "grape", "orange"]
    return random.choice(word_list)


def check_guess(word, guess):
    if len(guess) != len(word):
        return False

    for i in range(len(word)):
        if guess[i] == word[i]:
            print("O", end=" ")
        elif guess[i] in word:
            print("X", end=" ")
        else:
            print("_", end=" ")

    print()
    return guess == word


def play_wordle():
    word = generate_word()
    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        if check_guess(word, guess):
            print(
                f"Congratulations! You guessed the word '{word}' in {attempts} attempts.")
            break


play_wordle()
