# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем
# сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

a = int(input("Length:  "))
b = int(input("Width: "))


def to_box(side1, side2):
    if side2 == 0:
        return 0
    else:
        if side1 < side2:
            side1, side2 = side2, side1
        print("Lenth  width: " + str(side1) + ' ' + str(side2))
        print("Quantity of boxes:" + str(side1 // side2))
        return to_box(side2, side1 % side2)


to_box(a, b)

# result = []
#
# while(length > 0):
#     if length < width:
#         length, width = width, length
#     result.append(width)
#     length -= width
#
# print(result)