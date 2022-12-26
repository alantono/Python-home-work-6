# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]  --> 0 2 3
# -3 * -1 * 0 = 0,  Вывод: 0

# n = int(input('Введите n: '))
# list = []
# for i in range(2 * n + 1):
#     list.append(i - n)
# print('Список из N элементов', list)
# a, b, c = (map(int, input('Введите 3 индекса через пробел: ').split()))
# print('Произведение элементов на указанных индексах: ',
#       list[a] * list[b] * list[c])

# Решение (задачи приведенной выше) с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

n = int(input('Введите n: '))
list = [i - n for i in range(2 * n + 1)]
print('Список из N элементов', list)
a, b, c = (map(int, input('Введите 3 индекса через пробел: ').split()))
print('Произведение элементов на указанных индексах: ',
      list[a] * list[b] * list[c])