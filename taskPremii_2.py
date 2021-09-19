import math

prize = 0
credit, employers = map(int, input().split())
# employers = int(input())
# a, b = map(int, input().split())

# Считывание значений в массив счетов и рачёт суммы денег на счетах
balanceArray = []
sum_balanceArray = 0
for i in range(credit):
    temp = int(input())
    balanceArray.append(temp)
    sum_balanceArray += temp

# Массив отношения суммы на каждом счете к общей сумме денег на всех счетах
# Массив, который включает, скольким людям с каждого счёта можно заплатить
# Создали кортеж (тип tuple), который хранит остатот от деления Mod (0 элемент) и целую часть Div (1 элемент)
# Сохранили массив целых людей
arrDiv = []
# Сохранили сумму дробной части
dTemp = 0
for i in range(credit):
    # 1. Расчёт произведения доли счёта на количество людей и скольким людям с каждого счёта можно заплатить
    amountOfPeopleForBalance = (balanceArray[i] / sum_balanceArray) * employers
    # 2. Cохранение целой части и запоминание дробной (d) (может быть как 1, так и 2)
    arrModDiv = math.modf(amountOfPeopleForBalance)
    arrDiv.append(round(arrModDiv[1]))
    dTemp += arrModDiv[0]
d = round(dTemp)

# Определение максимальной премии
# Делим сумму счета на максимальное целое количество людей (k)
kMin = 1000000000
for i in range(len(arrDiv)):
    # Можно столкнуться с проблемой деления на 0. В высшей математике при делении на 0 получается бесконечность.
    # Исходя из этого правила, в данной задаче нужно записать в массив как можно большее число.
    # Оно в любом случае не будет максимально возможной премией.
    if arrDiv[i] == 0:
        kTemp = 1000000000
    else:
        kTemp = (balanceArray[i] / arrDiv[i])

    if kTemp < kMin:
        kMin = kTemp

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
    prize = kMin
else:
    prize = kPlusOne[d - 1]
print('Максимально возможная премия:', math.floor(prize))
