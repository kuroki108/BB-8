import random

number = random.randint(1, 10)
guess = None

print(f'Solution: {number}')

while guess != number:
    guess = int(input('Gebe eine Zahl ein...'))
    try:
        if guess < number:
            print('Too low.')

        elif guess > number:
            print('Too high')

        elif guess == number:
            print('You got it.')

    except ValueError:
        print('Value Error') 


print('See you next Time')