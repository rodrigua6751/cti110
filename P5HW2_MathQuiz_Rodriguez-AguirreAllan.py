# Simple math quizzes
# 04/29/21
# CTI-110 P5HW2 - Math Quiz
# Allan Rodriguez-Aguirre

import random

print('Welcome to Math Quiz')
print()

def add_num():
    random_num1 = random.randint(1,1000)
    random_num2 = random.randint(1,1000)
    solution = random_num1 + random_num2
    print('  ', random_num1)
    print('+ ', random_num2)
    print()
    count = 1
    guess = int(eval(input('Enter answer.\n')))
    while guess != solution:
        if guess > solution:
            print('Sorry, guess is too high.')
            print()
            guess = int(input('Try again: '))
            count += 1
        elif guess < solution:
            print('Sorry, guess is too low.')
            print()
            guess = int(input('Try again: '))
            count += 1
    print('Congratulations!!!! Your answer is correct..')
    print('Number of guesses:', count)
    
def subtract_num():
    random_num1 = random.randint(1,1000)
    random_num2 = random.randint(1,1000)
    solution = random_num1 - random_num2
    print('  ', random_num1)
    print('- ', random_num2)
    print()
    count = 1
    guess = int(input('Enter answer.\n'))
    while guess != solution:
        if guess > solution:
            print('Sorry, guess is too high.')
            print()
            guess = int(input('Try again: '))
            count += 1
        elif guess < solution:
            print('Sorry, guess is too low.')
            print()
            guess = int(input('Try again: '))
            count += 1
    print('Congratulations!!!! Your answer is correct..')
    print('Number of guesses:', count)

choice_num = True
while choice_num:
    print()
    print('MAIN MENU')
    print('--------------------')
    print('1. Add Random Numbers')
    print('2. Subtract Random Numbers')
    print('3. Exit')
    print()
    choice_num = int(input('Please choose one of the menu options: '))
    if choice_num == 1:
        add_num()
    elif choice_num == 2:
        subtract_num()
    elif choice_num == 3:
        print('Thank you for playing...')
        print('Bye!!')
        exit()
    else:
        print('Invalid. Please enter 1, 2, or 3.')
        print()
        
main()

# Import random to generate random numbers
# Generate two random numbers from 1,1000
# Ask user to select mode of adding or subtracting the random numbers
# When adding, calculate solution when adding two random numbers
# When subtracting, calculate solution when subtracting two random numbers
# Ask user to input guess of answer
# If guess is below correct answer, try again
# If guess is above correct answer, try again
# If guess is correct, congratulate user, show amount of guesses taken and prompt main menu
# If user selects 3, terminate program

