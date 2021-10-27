import random

def Systempick(limit):
    return random.randint(0, limit)

def NumGuess(tries, guess_range, system_guess):
    for i in range(1, tries+1):
        user_guess = int(input('\nMake a guess: '))
        if user_guess in guess_range:
            if user_guess == system_guess:
                print(f'\nYou won, with {i} try(s).')
                return True
            elif user_guess > (system_guess + 10):
                print(f'\nYour guess is too large, {(tries)-i} try(s) left.')
            elif user_guess < (system_guess - 10):
                print(f'\nYour guess is too small, {(tries)-i} try(s) left.')
            elif user_guess in range(system_guess , (system_guess + 11)):
                print(f'\nYour guess is larger, {(tries)-i} try(s) left.') 
            elif user_guess in range((system_guess - 11) ,system_guess + 1):
                print(f'\nYour guess is Smaller, {(tries)-i} try(s) left. ')
        else:
            print(f'Pick within the range, {(tries)-i} try(s) left.')
