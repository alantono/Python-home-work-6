# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# n = int(input('Введите n: '))
# list = []
# dictionary = {}
# sum = 0
# for i in range(1, n + 1):
#     list.append((1 + (1 / i))**i)
#     dictionary[i] = list[i - 1]
#     sum = sum + list[i - 1]
# print('Для n=', n, dictionary, 'Сумма', sum)

# Решение (задачи приведенной выше) с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

n = int(input('Введите n: '))
list1 = [i for i in range(1, n + 1)]
list2 = [round(((1 + (1 / i))**i), 2) for i in range(1, n + 1)]
result = list(zip(list1, list2))
print('Для n=', n, result)
