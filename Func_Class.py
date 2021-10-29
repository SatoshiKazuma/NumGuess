import random
from rich.console import Console 
console = Console()

def Systempick(limit):
    return random.randint(0, limit)

def NumGuess(tries, guess_range, system_guess):
    for i in range(1, tries+1):
        user_guess = int(input('\nMake a guess: '))
        if user_guess in guess_range:
            if user_guess == system_guess:
                console.print(f'\nYou won, with {i} try (s).',style='bold green')
                return True
            elif user_guess > (system_guess + 10):
                console.print(f'\nYour guess is too large, {(tries)-i} try (s) left.',style='red')
            elif user_guess < (system_guess - 10):
                console.print(f'\nYour guess is too small, {(tries)-i} try (s) left.',style='red')
            elif user_guess in range(system_guess , (system_guess + 11)):
                console.print(f'\nYour guess is larger, {(tries)-i} try (s) left.',style='red') 
            elif user_guess in range((system_guess - 11) ,system_guess + 1):
                console.print(f'\nYour guess is Smaller, {(tries)-i} try (s) left. ',style='red')
        else:
            console.print(f'Pick within the range, {(tries)-i} try (s) left.',style='red')
