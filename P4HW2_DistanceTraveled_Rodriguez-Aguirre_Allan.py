# CTI-110
# P4HW2 - Distance Traveled
# Allan Rodriguez-Aguirre
# 04/15/21

def valid_num(x):
    try:
        return float(x)
    except ValueError:
        return False

def main():

    speed_num = False
    while speed_num == False:
        speed = input('Enter car\'s speed: ')
        if valid_num(speed):
            speed = float(speed) 
            speed_num = True
        else:
            print('\nInvalid speed!')
            print()

    proceed_time = True
    while proceed_time == True:
        time_num = False
        time_error = '\nError ! Time entered should be >0'
        while time_num == False:
            time = input('\nEnter time traveled: ')
            if valid_num(time):
                if float(time) <= 0:
                    print(time_error)
                else:
                    time = float(time)
                    time_num = True
            else:
                print(time_error)

        print('{:<6} {:<6}'.format('Time', 'Distance')) 
        print('---------------------')

        for i in range(1, int(time)):
            print('{:<6} {:<6}'.format(i, i * speed))

        if str(time).endswith('.0'):
            print('{:<6} {:<6}'.format(int(time), time * speed))
        else:
            print('{:<6} {:<6}'.format(int(time), int(time) * speed))
            print('{:<6} {:<6}'.format(time, time * speed)) 
        
        valid = False
        while valid == False:
            add_input = input('Would you like to enter a different time? (y for yes): ')
            if add_input == 'n':
                proceed_time = False
                valid = True
            elif add_input == 'y':
                valid = True
            else:
                print('\nInvalid input!')
                print()
               
main()

#Processes input to see if it will calculate as an error
#Assure input is valid as a float
#Ask user to enter speed
#Assures input for speed is valid
#Converts input to float
#Ask user to enter time
#If user inputs invalid data, an error message is prompted
#A tabular view of information is displayed
#Calculates time and speed ranging from 1 to number input of time
#Allows float as last entry
#Mulitiplies i in range and speed
#Ask user if additional time input is desired
#If yes, user is asked to enter time again
#If no, the program closes

