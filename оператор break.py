# break - штука, которая немедленно прерывает выполнение программы

for i in range(10):
    print('Итерация номер', i, 'начинается')
    if i == 3:
        print('Выход из цикла, внезапно, правда?')
        break
    print('Итерация номер', i, 'успешно завершена')
print('Цикл завершён')