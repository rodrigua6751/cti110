# CTI-110
# P3HW2 - Distance Traveled
# Allan Rodriguez-Aguirre
# 03/25/21


first_num = float(input('Enter car\'s speed: '))
sec_num = float(input('Enter time traveled: '))
product = first_num * sec_num

def main():
    print('Speed entered:', first_num)
    print('Time entered:', sec_num)
    print()
    print('Distance Traveled', product, 'miles')

if sec_num <= 0:
    print()
    print('Error! Time entered should be > 0')
    sec_num = 1
    product = first_num * sec_num
    print()
    print('Speed entered:', first_num)
    print('Time entered:', sec_num)
    print()
    print('Distance Traveled', product, 'miles')
else:
    main()
    

#Input first number indicating speed
#Input second number indicating time
#If input is less than 0, error message is displayed
#Display first number
#Displays 1 as second number
#Calculates both first and second number
#Else if input is greater than 0, main function is used
#Display first number
#Display second number
#Calculate product of first and second number when multiplied
