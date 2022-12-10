# def hellow():
#     print('hellow')
# def hellow(name):
#     print(f'hellow{name}')

# hellow('薛')

# def my_min(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# a = my_min(1,2)
# print('my_min:', a)

import random as r

r.randint(1.6)


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(r.randint(1, 6))
    return dice


cnt = int(input('輸入丟色子的次數:'))
print(roll_dice)
