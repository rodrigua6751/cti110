# CTI-110
# P2HW2 - Lists and Sets
# Allan Rodriguez-Aguirre
# 03/11/21

a_num = int(input('Enter a value: '))
b_num = int(input('Enter a value: '))
c_num = int(input('Enter a value: '))
d_num = int(input('Enter a value: '))
e_num = int(input('Enter a value: '))
f_num = int(input('Enter a value: '))
g_num = int(input('Enter a value: '))
h_num = int(input('Enter a value: '))
i_num = int(input('Enter a value: '))
j_num = int(input('Enter a value: '))

num_list = [a_num, b_num, c_num, d_num, e_num, f_num, g_num, h_num, i_num, j_num]
avg_list = sum(num_list)/len(num_list)

print('Lowest number entered:', min(num_list))
print('Highest number entered:', max(num_list))
print('Total of all numbers entered:', sum(num_list))
print('Average of numbers entered:', avg_list)

num_set = set(num_list)
print()
print(num_set)

#Input 10 numbers
#Create list for numbers entered
#Calculate average for numbers entered
#Display min of numbers entered
#Display max of numbers entered
#Display sum of numbers entered
#Display average of numbers entered
#Convert list to set
#Display set content
