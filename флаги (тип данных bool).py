# ---------------------------------------------------------------
# | Изначально флаг устанавливается в False, затем програ       |
# | работает и послед выполненных действий флаг устанавливается |
# | в True. После идёт проверка "поднят ли флаг", по её         |
# | результатам выполняются те или иные действия.               |
# ---------------------------------------------------------------

forbidden_word = 'синхрофазотрон'
print('Введи 10 слов, но постарайся не вводить слово "' + forbidden_word + '"')

said_forbidden_word = False

for i in range(10):

    if said_forbidden_word:
        print('Помни, нельзя писать "'+ forbidden_word + '"')

    word = input()
    if word == forbidden_word:
        said_forbidden_word = True

if said_forbidden_word:
    print('Ты нарушил условие')
else:
    print('Спасибо, что воздержался')