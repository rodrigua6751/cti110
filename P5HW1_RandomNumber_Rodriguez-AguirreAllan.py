# Random Number Game - Player Attempts to Guess Random Generated Number
# 4/27/21
# CTI-110 P5HW1 - Random Number
# Allan Rodriguez-Aguirre

import random

def main():
    random_num = random.randint(1,100)
    guess = int(input('Enter a number between 1 and 100: '))
    while guess != random_num:
        if guess > random_num:
            print('Too high, try again.')
            guess = int(input('Enter a number between 1 and 100: '))
        elif guess < random_num:
            print('Too low, try again.')
            guess = int(input('Enter a number between 1 and 100: ')) 
    print('Congratulations!!!')
    play_again = int(input('Would you like to play again? (1 - yes, 2 - no)'))
    if play_again == 1:
        choice_num = True
    elif play_again == 2:
        exit()
    else:
        print('Invalid. Please enter 1 or 2.')
        print()

choice_num = True
while choice_num:
    print()
    print('MAIN MENU')
    print()
    print('-----------------')
    print()
    print(' 1.) Play Game')
    print(' 2.) Exit')
    print()
    print()
    print()
    choice_num = int(input())
    if choice_num == 1:
        main()
    elif choice_num == 2:
        exit()
    else:
        print('Invalid. Please enter 1 or 2.')
        print()

main()

# Import random to generate random number
# Generate random number between 1-100
# Ask user to input guess of number
# If guess below random number is high, try again
# If guess above random number is low, try again
# Ask user to input if they want to play again
# If user inputs to play again, return main menu with options
# If user inputs exit, terminate program
