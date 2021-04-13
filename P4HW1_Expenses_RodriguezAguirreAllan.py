#CTI-110
#P4HW1 - Expenses
#Allan Rodriguez-Aguirre
#04/13/21

amount = float(input('Enter starting amount in account: $'))
print()

def main():
    expense = 0.0
total_expenses = 0
num_expenses = 0
yesNo='\0'
while yesNo !='n' and yesNo !='N':
    expense=float(input('Enter expense {0}: '.format((num_expenses + 1))))
    num_expenses += 1
    total_expenses += expense
    yesNo = input('Do you want to enter another expense? (y/n) ')
    if yesNo =='n' or yesNo =='N':
        print('\nAmount in account before expenses subtracted: ${0:.1f}'.format(amount))
        amount -= total_expenses
        print('Number of expenses entered: {0}'.format(num_expenses))
        print('Amount in account after expenses subtracted is ${0:.1f}'.format(amount))
    print()
if __name__ == '__main__':
    main()
