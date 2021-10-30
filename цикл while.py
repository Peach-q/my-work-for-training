total = 0
print('Вводи цены, для остановки введи -1')

price = int(input())
while price > 0:
    total += price
    price = int(input())

print('Общая стоимость равна', total)
