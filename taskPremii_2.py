import math

prize = 0
credit, employers = map(int, input().split())
# employers = int(input())
# a, b = map(int, input().split())

balanceArray = sorted([int(input()) for i in range(credit)])
# Рачёт суммы денег на счетах
sum_balanceArray = sum(balanceArray)
# Массив отношения суммы на каждом счете к общей сумме денег на всех счетах
ratioArray = []
for i in range(len(balanceArray)):
    ratioArray.append(balanceArray[i] / sum_balanceArray)
# print(ratioArray)

# Расчёт скольким людям с каждого счёта можно заплатить
# 1. Расчёт произведения доли счёта на количество людей
amountOfPeopleForBalance = []
for i in range(len(ratioArray)):
    amountOfPeopleForBalance.append(ratioArray[i] * employers)
# print(amountOfPeopleForBalance)

# 2. Cохранение целой части и запоминание дробной (d) (может быть как 1, так и 2)
# Создали кортеж (тип tuple), который хранит остатот от деления Mod (0 элемент) и целую часть Div (1 элемент)
arrModDiv = []
for i in range(len(amountOfPeopleForBalance)):
    arrModDiv.append(math.modf(amountOfPeopleForBalance[i]))
# print(arrModDiv)

# Сохранили массив целых людей
arrDiv = []
for i in range(len(arrModDiv)):
    arrDiv.append(round(arrModDiv[i][1]))
# print(arrDiv)

# Сохранили сумму дробной части
dTemp = 0
for i in range(len(arrModDiv)):
    dTemp += arrModDiv[i][0]
d = round(dTemp)
# print(d)

# Определение максимальной премии
# Делим сумму счета на максимальное целое количество людей (k)
kTemp = []
k = []
for i in range(len(arrDiv)):
    # Можно столкнуться с проблемой деления на 0. В высшей математике при делении на 0 получается бесконечность.
    # Исходя из этого правила, в данной задаче нужно записать в массив как можно большее число.
    # Оно в любом случае не будет максимально возможной премией.
    if arrDiv[i] == 0:
        kTemp.append(1000000000)
    else:
        kTemp.append(balanceArray[i] / arrDiv[i])
k = sorted(kTemp)
# print(k)

# Делим сумму счета на максимальное целое количество людей (k+1)
kPlus1 = []
kPlusOneTemp = []
kPlusOne = []
for i in range(len(arrDiv)):
    kPlus1.append(arrDiv[i] + 1)
# print(kPlus1)
for i in range(len(kPlus1)):
    kPlusOneTemp.append(balanceArray[i] / kPlus1[i])
kPlusOne = sorted(kPlusOneTemp, reverse=True)
# print(kPlusOne)

# если остаток людей = 0, то берём минимум из массива k, иначе массив (k+1) сортируем по убыванию
# и берем элемент, индекс которого равен d (если d=1,то берём первй элемент, если d=2, то второй)
if d == 0:
    prize = k[0]
else:
    prize = kPlusOne[d - 1]
print('Максимально возможная премия:', math.floor(prize))
