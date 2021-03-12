# 1 
# Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за 4 квартал (т.е. 4 числа) 
# для каждого предприятия. Программа должна определить 
# среднюю прибыль (за год для всех предприятий) и отдельно 
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего

from collections import defaultdict

corps = defaultdict(list)

corps_count = int(input('Введите количество предприятий: '))

i = 0

while i < corps_count:
    name = input('Введите название предприятия: ')

    pr_list = []

    for j in range(4):
        prib = input('Введите прибыль за {} квартал: '.format(j + 1))
        pr_list.append(prib)

    corps[name].extend(pr_list)
    i += 1

print(corps)

middle = 0
dc_corps = dict(corps)


for itr in dc_corps.values(): # Перебераем значения в словаре
    for j in itr:
        middle = middle + int(j)

middle = middle / (corps_count * 4) # Подсчет средней прибыли (для всех предприятий)

print("Средняя прибыль: {} (для всех предприятий)".format(middle))

for key in dc_corps:
    middle_comp = 0
    for it in dc_corps[key]:
        middle_comp += int(it) / 4
    print(middle_comp)

    if middle_comp < middle:
        print("Доход компании {} Ниже среднего!".format(key)) # Выводим ответ (ниже)
    else:
        print("Доход компании {} Выше среднего!".format(key)) # Выводим ответ (выше)

