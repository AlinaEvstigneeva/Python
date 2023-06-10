# print(5, 8, 6)

# int - целые числа 
# float - дробные числа
# bool - логический тип данных ( true/false)
# str - строка

# объявление переменной     название переменной = значение переменной (один знак равенства - присвоение значения к переменной)
# программный код:              Вывод:
#   a = 123                         123
#   b = 1.23                        1.23
#   print(a)
#   priint(b)

#n = 5
#print(n)

# n = None  - если мы пока не знаем какой тип данных будет присовен переменной

# тип данных str прописывается в ковычках одинарных или двойных
# n = 'asdfg'
# n1 = "lkjh"


# для того, чтобы узнать какой тип данный используется вводим:
# n = 'lkjh'
# print(type(n))


# чтобы прописать кавычки в строке прописываем \(слэш) перед кавычкой или двойные кавычки
# n = 'lk\'hgfd'
# n1 = 'asd"fghjk"rtyui'


# для комментирования одной строчки перед ней прописывается (#)
# для многострочного комментирования используются тройные апострофы в начале и в конце строк("""  """)


# Интерполяция - получение сложной строки из несколькихх простых с помощью шаблонов
# a = 5
# b = 5.89
# c = 'hello'

# print(a,b,c) - вывод всех переменных в одну строку.

# print(a, ' - ', b, ' - ', c) - запись через дефис
# print(f" {a} - {b} - {c}") - интерполяция (первый шаблон) на питоне
# print("{} - {} - {}".format(a,b,c)) - второй вариант шаблона интерполяции. 


# Ввод данных 
# Команда для ввода данных : input() - после запуска команды в консоли появится курсор, призывающий ввести данные.
# В таком случае input() введенное значение в консоли нигде не сохраняется.
# Чтобы его сохранить, необходимо ввести переменную  a = input()

# print('Введите первое число: ') - приглашение для ввода данных в консоль (1вариант - ввод начинается с новой строки)
# b = input('Введите второе число: ') - 2 вариант - ввод начинается сразу после двоеточия, правее

# a = input()
# print(a) -  сразу напечатаем сохраненный результат в консоли 


# Приведение к типу данных

# c = 5.89
# print(c)
# n = int(c) - функция int отбрасывает дробную часть и float становится int. Так же работет bool и str.
# print(n)

# input() - данная команда автоматически сохряняет данные в типе данных str.
# Чтобы произвести сложение/вычитание/умножение и тд, необходимо тип str сразу перевести в int
# Для этого мы сразу прописываем код следующим образом:

# print('Введите первое число: ')
# a = int(input())                             - сразу приводим тип str в int
# b = int(input('Введите следующее число: '))
# print(a, ' + ', b, ' = ', a + b) - обращаем внимание на все запятые


# Арифметические операции в питоне

# + сложение 
# - вычитание
# * умножение
# / деление(по умолчанию в вещественных числах)
# % остаток от деления
# // целочисленное деление
# ** возведение в степень


# Округление чисел

# a = 5.6789
# b = 6.5678
# print(a * b)

# round(1.345678, 2) - округляющая функция.  
# Первый аргумент - число, которое хотим округлить, второй аргумент - сколько знаков долдно остаться после запятой.

# Новый вариант записи, сразу с округлением:
# a = 5.6789
# b = 6.5678
# print(round(a * b, 2))


# Сокращенные присваивания.

# В C# это выглядело так: i++ , т.е. i увеличивалось на единицу

# В питоне это выглядит следующим образом:
# iter = 2
# iter += 3  - iter = iter + 3
# iter -= 4  - iter = iter - 4
# iter *= 5  - iter = iter * 5
# iter /= 5  - iter = iter / 5
# iter //= 5  - iter = iter // 5
# iter %= 5  - iter = iter % 5
# iter **= 5  - iter = iter ** 3


# Логические операции

# > больше
# >= больше или равно
# < меньше
# <= меньше или равно
# == равно (проверяет, равны ли числа)
# != не равно (проверяет, не равны ли значения)
# not не(отрицаение)
# and и(конъюнкция)
# or или(дизъюнкция)


# Управляющие конструкции: if, if-else.
# В С# используются фигурные скобки для выполнения какого-либо действия.
# В Пионе вместо скобок используют отступы. Один отступ - 1 нажатие TAB или 4 пробела.

# if condition:
#     operator 1
#     operator 2
#     ...
#     operator n
# else:
#     operator n + 1
#     operator n + 2
#     ...
#     operator n + m


# Еще один вариант использования операторов else-if в связке с elif (else if).

# if condition:       - если выполняется условие if, то выполняется оператор и проверка дальше не идет.
#     operator
# elif condition 2:   - если if не проходит проверку, то проверяется условие 2 и выполняется оператор.
#     operator
# elif condition 3:   - если условие 2 тоде не проходит проверку, проверяется условие 3 и вып-ся оператор.
#     operator
# else:               - если все условия не прошли проверку, то выполняется блок кода else.
#     operator

# Пример:

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


# Сложные условия.

# if condition1 and condition2:   - оператор выполнится, когда оба условия окажутся верными
#     operator

# if condition1 or condition2:    - оператор выполнится, когда хотя бы одно из условий окажется верным.
#     operator



# Цикл While.

# while condotion:
#     operator 1
#     operator 2
    
# Пример:

# n = 423
# summa = 0 
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)



# Управляющие конструкции: while-else

# while condition:
#     operator 1
#     operator 2
#     ...
#     operator 
# else:
#     operator n + 1 
#     operator n + 2
#     ...
#     operator n + m


# Пример:

# i = 0
# while i < 5:        - цикл выполняется пока i меньше 5
#     if i == 3:      - если i становится равно 3, то цикл прерывается и сразу переходит на этап print(i)
#         break           команду break лучше не использовать, это не является хорошим тоном программирования.
#     i = i + 1       - при поледующий итерациях i увеличивается на 1
# else:
#     print('Пожалуй')
#     print('хватит)')
# print(i)

# Чтобы избежать использование команды break, можно воспользоваться методом флагов.

# n = int(input())
# flag = True
# i = 2
# while flag:     - тут мы уже подразумеваем, что flag = True
#     if n % i == 0:  - если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2:    делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#     i += 1



# Цикл for, функция range.
# В основном используется для перебора значений.

# for i in enumeration
#     operator 1
#     operator 2
#     ...
#     operator n

# Пример:

# for in 1, -2, 3, 14, 5
#     print(i)                    результат: 1 -2 3 14 5


# Функция range генерирует какую-то последовательность.
# В этой функции мб 3 аргумента
# 1 - откуда начинаем (по умолчанию начинаем с нуля)
# 2 - на каком числе мы заканчиваем
# 3 - шаг (по умолчанию единица)

# r = range(5)    0 1 2 3 4 - генерируется последовательность, не включая аргумент
# r = range(2, 5)     2 3 4 - начинаем с 2 и заканчиваем, не включая второй аргумент
# r = range(0, -5)    ---- - тк шаг всегда единица, мы не можем от 0 дойти до -5
# r = range(1, 10, 2)     1 3 5 7 9 - добавился шаг в две единицы (3й аргумент)
# r = range(100, 0, -20)      100 80 60 40 20 - если шаг с минусом, значит отнимаем его 

# Пример:

# r = range(100, 0, -20)
# for i in r:
#     print(i)


# Цикл for может использоваться также со строками, тк они тоже имеют нумерацию, такую же как у массивов,
# начиная с нуля.

# a = 'qwerty'
# for i in a:
#     print(i)

# Сложный цикл. Пример:

# line = ""             - создаем пустую строку
# for i in range(5):    - создаем последовательность для того, чтобы цикл прошел 5 раз
#     line = ""         - создаем еще одну пустую строку
#     for j in range(5):    - и в ней создаем последовательность, включающую в себя 5 знаков
#         line += "*"       - все время прибавляем звездочку
#     print(line)           - печатаем первый цикл (нет пробела перед принт!)


# Еще немного о сроках:

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'

# Функции:
# print(len(text))    - позволяет узнать размер нашей строки
# print('ещё' in text)    - ищет заданную строку в нашей сроке, результат: True или False
# print(text.lower())   - позволяет перевести все буквы в нашей строке в нижний регистр
# print(text.upper())     - позволяет перевести все буквы в верхний регистр
# print(text.replace('ещё', 'ЕЩЁ'))   - позволяет заменить участок текста. 1 аргумент - то, что заменяем
#                                                                         2 аргумент - то, чем заменяем



