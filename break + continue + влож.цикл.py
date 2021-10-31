# Вывод таблицы умножения, кроме столбика k

print('Тренажер по вводу палиндрома')
while True:
    print('Введите число палиндром:')
    number = n = int(input())
    reverse = 0

    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10

    if number == reverse:
        print('Вы ввели палиндром, программа остановлена')
        break
    print('Введённое число не палиндром, попробуй ещё раз')