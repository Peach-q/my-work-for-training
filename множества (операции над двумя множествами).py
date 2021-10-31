# Есть 4 операции, позволяющие что-то делать со множествами:
#
#    -объединение
#    -пересечение
#    -разность
#    -симметричная разность

# Объединение - включает в себя все элементы, которые есть хотя бы в одном из них
# Можно использовать:
#        - .union()
#        - |
my_set_one = {'a', 'b', 'c'}
my_set_two = {'e', 'f'}

union_set = my_set_one.union(my_set_two)
print('Объединение с помощью метода .union() :', union_set)

two_union_set = my_set_two | my_set_one
print('Объединение с помощью оператора | :', two_union_set)
print('------------------------------------------------')

# Пересечение - включает в себя все элементы, которые есть в обоих множествах
# Можно использовать:
#        - .intersection()
#        - &
my_set_one = {'a', 'b', 'c'}
my_set_two = {'e', 'f', 'b', 'c'}

intersection_set = my_set_one.intersection(my_set_two)
print('Пересечение с помощью метода .intersection() :', intersection_set)

two_intersection_set = my_set_two & my_set_one
print('Пересечение с помощью оператора & :', two_intersection_set)
print('------------------------------------------------')

# Разность - включает в себя все элементы, которые есть в первом множестве, но которых нет во втором
# Можно использовать:
#        - .difference()
#        - -

my_set_one = {'a', 'b', 'c'}
my_set_two = {'e', 'f', 'b', 'c'}

difference_set = my_set_one.difference(my_set_two)
print('Разность с помощью метода .difference() :', difference_set)

two_difference_set = my_set_two - my_set_one
print('Разность с помощью оператора - :', two_difference_set)
print('------------------------------------------------')

# Симметричная разность - включает в себя все элементы, которые есть только в одном из этих множеств
# Можно использовать:
#        - .symmetric_difference()
#        - ^

my_set_one = {'a', 'b', 'c'}
my_set_two = {'e', 'f', 'b', 'c'}

difference_set = my_set_one.symmetric_difference(my_set_two)
print('Симметричная разность с помощью метода .symmetric_difference() :', difference_set)

two_difference_set = my_set_two ^ my_set_one
print('Симметричная разность с помощью оператора ^ :', two_difference_set)
print('------------------------------------------------')