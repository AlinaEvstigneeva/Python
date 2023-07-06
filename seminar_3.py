# lst = []
# for i in range(1, 30):
#     lst.append(i)
# print(lst)


# a = [i for i in range(1 ,20) if i % 2 == 0]     #если у нас есть условие только if то его прописываем после цикла
# print(a)

a = [i if i % 2 == 0 else 0 for i in range(1 ,20) ]     #если есть еще условие else, то все условие прописываем до цикла
print(a)