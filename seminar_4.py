# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

str_1 = input('Введите строку, прописыпая каждый знак через пробел: ').split()
print(str_1)
count = 0

for i in range(len(str_1)):
    for j in range(i + 1,len(str_1)):
        if str_1[i] == str_1[j]:
            count += 1
            str_1[j] += '_' + str(count)
    count = 0 
print(str_1)