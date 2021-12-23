import random

sick_days = random.randint(0, 10)
print('Initial sick days: ', sick_days)

while sick_days:
    actually_sick = random.choice([True, False])
    kinda_sick = random.choice([True, False])
    dont_feel_like_it = random.choice([True, False])

    calling_in_sick = True if (actually_sick and sick_days > 0) or (
            kinda_sick and dont_feel_like_it and sick_days > 0) else False

    if calling_in_sick:
        sick_days -= 1
    print(f'Called in sick today: {calling_in_sick}')
    print('Sick days remaining: ', sick_days, '\n')
print('No more sick days left.')

