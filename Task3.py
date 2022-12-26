# Реализуйте алгоритм перемешивания списка.

# from random import randint
# list = []
# for i in range(11):
#     list.append(i)
# print('Исходный список: ', list)
# list1 = []
# for i in range(len(list)):
#     n = randint(0, len(list) - 1)
#     list1.append(list[n])
#     del list[n]
# print('Перемешанный список: ', list1)

# Решение (задачи приведенной выше) с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

from random import randint
list = [i for i in range(11)]
print('Исходный список: ', list)
list1 = []
for i in range(len(list)):
    n = randint(0, len(list) - 1)
    list1.append(list[n])
    del list[n]
print('Перемешанный список: ', list1)
