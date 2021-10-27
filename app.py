from Func_Class import *

print('Number Guessing program\n')

guess_range_cap = int(input('Pick a range to guess from, It starts from zero : '))
guess_range = range(0, guess_range_cap+1)
system_guess = Systempick(guess_range_cap)
tries = int(input('How many tries do you want: '))
chances = (((guess_range_cap**(-1))*tries)*100)

if not NumGuess(tries, guess_range, system_guess):
    print(f'\nYou could not guess the correct answer, the number was {system_guess} ')

print(f'Your chances of guessing right were at {round(chances, 4)}%')