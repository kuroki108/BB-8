import random
import time

def get_user_choice():
    user_choice = input('rock, paper, or scissors? ')
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input('Please choose Rock, Paper, or Scissors:')
    return user_choice

def get_ai_choise():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choise, ai_choise):
    if user_choise == ai_choise:
        return 'Its a tie!'
    elif(
        (user_choise == 'rock' and ai_choise == 'scissors') or 
        (user_choise == 'scissors' and ai_choise == 'paper') or 
        (user_choise == 'paper' and ai_choise == 'rock')):
        return 'You win!'
    else:
        return 'AI wins!'
    
while True:
    user_choice = get_user_choice()
    ai_choise = get_ai_choise()
    time.sleep(2)
    print(f'You chose {user_choice}, and Ai chose {ai_choise}.')
    result = determine_winner(user_choice, ai_choise)
    print(result)
    play_again = input('Play again? (y/n): ')
    if play_again != 'y':
        break