# 2 
# Написать программу сложения и умножения двух положительных 
# целых шестнадцатеричных чисел. При этом каждое число представляется 
# как коллекция, элементы которой — цифры числа


from collections import deque

num1 = input('Введите первое 16 х число: ')
num2 = input('Введите второе 16 х число: ')

print(num1)
print(num2)

result = deque()

# ничего другого не придумал:
dict1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


if len(num1) > len(num2):
    x = deque(num1)
    y = deque(num2)

else:
    x = deque(num2)
    y = deque(num1)

mind = 0
while x:

    if y:
        answer = dict1[x.pop()] + dict1[y.pop()] + mind

    else:
        answer = dict1[x.pop()] + mind

    mind = 0

    if answer < 16:
        result.appendleft(dict1[answer])

    else:
        result.appendleft(dict1[answer - 16])
        mind = 1

if mind:
    result.appendleft('1')

print(result)


