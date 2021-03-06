

my_set = {'a', 'b', 'c'}    # вычисление кол-ва элементов во множестве   -------------------
n = len(my_set)             #                                            | тут n = 3       |
                            # для этого служит функция len               -------------------

my_set = {'a', 'b', 'c'}   # вывод элементов множества
print(my_set)
print('----------------------------------------------------------------------------------------------')

# обход элементов множества в цикле
my_set = {'a', 'b', 'c'}
for elem in my_set:
    print(elem)
print('----------------------------------------------------------------------------------------------')

#проверка наличия элементов во множестве
my_set = {'a', 'b', 'c'}

# elem = 'z' <- небольшая модификация для поиска конкретного элемента во множестве

if elem in my_set:
    print('Элемент находится во множестве')
else:
    print('Элемента во множестве нет')
print('----------------------------------------------------------------------------------------------')

#добавление элемента во множество
my_set = {'a', 'b', 'c'}               # в этом помогает .add()
new_elem = 'e'
my_set.add(new_elem)
print(my_set)

#удаление элемента можно реализовать четырьмя способами:
#      -.discard() (если элемент есть во множестве, то удаляет; если элемента нет во множестве - ничего не делает)
#      -.remove()  (удалить заданный элемент, если он есть; породить ошибку KeyError, если элемента нет во множестве)
#      -.pop()     (удаляет некоторый эдемент из множества и возвращает его как результат)
#      -.clear()   (полностью очищает множество ото всех элементов)

my_set = {'a', 'b', 'c'}

my_set.discard('a') #Удалён
my_set.discard('hello') #Не удалён, ошибки нет

my_set.remove('b') #Удалён
print(my_set)
# my_set.remove('word') #Не удалён, порождена ошибка KeyError
print('----------------------------------------------------------------------------------------------')

my_set = {'a', 'b', 'c'}
print('До удаления', my_set)
elem = my_set.pop()
print('Удаленный элемент', elem)
print('После удаления', my_set)
print('----------------------------------------------------------------------------------------------')

my_set = {'a', 'b', 'c'}
print('До удаления', my_set)
my_set = my_set.clear()
print('После удаления', my_set)
print('----------------------------------------------------------------------------------------------')