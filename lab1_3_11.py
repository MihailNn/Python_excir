# Сформировать одномерный список целых чисел A, используя генератор случайных чисел
# (диапазон от 0 до 99). Размер списка n ввести с клавиатуры.
# Удалить пять первых нечетных по значению элементов списка.
import random

n = int(input("Input size of list :"))
array = []
count = 0
for i in range(n):
    randNum = random.randint(0, 99)
    array.append(randNum)
print(array)

i = 0
while i < len(array) and count < 5:
    print(len(array), count, array[i])
    if array[i] % 2 != 0:
        array.remove(array[i])
        i -= 1
        count += 1
    i += 1
print(array)

