# name = input()
# print(f"Привет, {name}")


# Написать программу, которая по возрасту определяет старый человек или молодой.

# age = int(input("Введите возраст: "))
# if age < 12:
#     print("Ребенок")
# elif age < 45:
#     print("Средних лет")
# else:
#     print("Зрелый человек")



# Целочисленное деление и остаток от деления.

# cost = 145
# money = 200
# print(money // cost, "купили вещей")
# print(money % cost, "осталось денег")



# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# n = int(input("Введите количество километров: "))
# m = int(input("Введите длину маршрута: "))

# result = m/ n 

# if m % n > 0:
#     result = int(result)        -  используя конструкцию if
#     result += 1

# result = m //n + int(m % n > 0)   - без конструкции if, как указано в условии

# print(f"Количество дней равно {result}")



# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.


# class1 = int(input("Введите количество учеников в первом классе: "))
# class2 = int(input("Введите количество учеников во втором классе: "))
# class3 = int(input("Введите количество учеников в третьем классе: "))

# result1 = class1 // 2 + int(class1 % 2 > 0)
# result2 = class2 // 2 + int(class2 % 2 > 0)
# result3 = class3 // 2 + int(class3 % 2 > 0)

# print(f" Для первого класса потребуется {result1} парт, для второго - {result2} и для третьего - {result3}")



# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

# i = int(input("Введите номер вагона: "))
# j = int(input("Введите номер текущего вагона: "))
# if i == j:
#     print("Недостаточно данных")
# else:
#     print(f" В электичке {i + j - 1} вагонов")



# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# a = int(input("Введите год: "))
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print("YES")
# else:
#     print("NO")




# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на одну клетку. 
# Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.
# Программа на вход получает четыре числа от 1 до 8 каждое, задающие номер столбца и строки сначала для первой клетки, 
# потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую
# или NO в противном случае. 
# В случе, если хотя бы одно из введенных чисел не входит в диапазон от 1 до 8, выведите строку "Ошибка!".

# first_v = int(input("Введите номер столбца для ПЕРВОЙ клетки: "))
# first_g = int(input("Введите номер строки для ПЕРВОГОЙ клетки: "))
# sec_v = int(input("Введите номер столбца для ВТОРОЙ клетки: "))
# sec_g = int(input("Введите номер строки для ВТОРОЙ клетки: "))

# def checkInput (first_v, first_g, sec_v, sec_g):    # Проверка на дурака с помощью метода
#     if(first_v in range (1,9)                     # В условии проверяем введенные числа с помощью диапазона range()
#        and first_g in range (1,9)                 # если мы прверяем несколько чисел в одном условии,
#        and sec_v in range (1,9)                   #  то записываем их через and
#        and sec_v in range (1,9)):
#         return True                              # Обязательно возвращаем из метода число, которое прошло проверку
#     else:
#         return False                            # Если число проверку не прошло, то мы возвращаем false 
    

# def cheas (first_v, first_g, sec_v, sec_g):
    
#     if(checkInput (first_v, first_g, sec_v, sec_g)):
#         if(abs(sec_v - first_v) <=1 and abs(sec_g - first_g) <=1):      # используется модуль abs, я хз, что это такое 
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("Ошибка!")


# cheas(first_v, first_g, sec_v, sec_g)       #Вызываем метод