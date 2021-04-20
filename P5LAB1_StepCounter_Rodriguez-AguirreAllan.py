def steps_to_miles(user_steps):
    miles = user_steps / 2000
    return miles

if __name__ == '__main__':
    user_steps = int(input())
    miles = user_steps / 2000
    print('{:.2f}'.format(steps_to_miles(user_steps)))