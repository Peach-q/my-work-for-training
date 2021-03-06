# Вложенный цикл - это один цикл, который находится внутри другого цикла
# Такие циклы используют, когда на каждой итерации одного цикла необходимо выполнить другой цикл
# Основное требование ко вложенным циклам:
#                                           --------------------------------------------------------
#                                           | все действия вложенного цикла лежали внутри внешнего |
#                                           --------------------------------------------------------
#
# Пример:
#           Необходимо вывести строку таблицу умножениия для заданного числа

k = int(input())
for i in range(1, 10):
    print(i, '*', k, '=', k*i, sep='', end='\t')

print('\n----------------------------------------------------')

# А если надо вывести таблицу умножения для всех чисел от 1 до k ?

k = int(input())                                                     # Выполнение работы программы начинается со внешнего цикла
for j in range(1, k+1):                                              # Итератор j менает свои значения от 1 до k (чтобы включить число k в расматриваемый промежуток, надо указать k+1)
 for i in range(1, 10):                                              # Затем происходит проверка: j < k+1
    print(i, '*', j, '=', j * i, sep='', end='\t')                   #    - В случае соблюдения условия выполняется внутренний цикл
                                                                     # Во внутреннем цикле i постоянно увеличивается на 1, значение дойдёт до 9
print('\n----------------------------------------------------')      # По такому же принципу во внешнем цикле с каждой итерацией j увеличивается на 1
