# программа не выполнится больше 3 раз

count = 0
total = 0
while count < 3:
    price = int(input())
    total += price
    count += 1
print(total)
