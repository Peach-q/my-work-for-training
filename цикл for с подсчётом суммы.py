# идёт подсчёт суммы всех значений, которые меньше данного

n = int(input())
total = 0
for i in range(n):
    total += i
    print('Промежуточная сумма', total)
print('Сумма всех членов равна', total)