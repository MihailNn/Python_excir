# Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
# mas = [5, 17, 3]
# biggerNum = 0
# for i  in range(0, len(mas)):
#     if biggerNum < mas[i]:
#         biggerNum = mas[i]
# print(biggerNum)

a = 5
b = 17
c = 19
d = a
if d < b:
    d = b
if d < c:
    d = c
print(d)