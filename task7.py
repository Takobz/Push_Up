import re

def read_dictionary():
    dictionary = {}
    my_input = str(input())
    i = 0;
    while (my_input != '###'):
        dictionary[i] = my_input
        my_input = str(input())
        i += 1
    
    return dictionary


def compute_response(target, guess):
    my_list = []
    response = ''

    for i in range(0, len(target)):
        my_list.append('.')


    print("You guessed " + guess)
    for i in range(0, len(guess)):
        for j in range(0, len(target)):
            if(guess[i] == target[j]):
                my_list[i] = guess[i]

    for letter in my_list:
        response += letter
                
    return response


def is_valid(guess, dictionary):
    for key in dictionary:
        if(dictionary[key] == guess):
            return True

    return False

"""
DO NOT MODIFY ANY CODE BELOW THIS LINE
"""

import random

dictionary = read_dictionary()

rng = random.Random(0)

while True:

    choice = input("Play a game? (Y/N): ")
    if choice == 'N':
        break

    target = dictionary[rng.randint(0, len(dictionary) - 1)]
    turns = 0
    MAX_TURNS = 6
    while True:
        if turns == MAX_TURNS:
            print("Game over! :(")
            print('The word was: {}'.format(target))
            break
        else:
            guess = input()
            while not is_valid(guess, dictionary):
                print('{} is not a valid word!'.format(guess))
                guess = input()

            print("You guessed: {}".format(guess))
            response = compute_response(target, guess)
            print('Response: {}'.format(response))
            if response == guess:
                # we won!
                print("You win! :)")
                break
        turns += 1

