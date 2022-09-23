# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Введите X, Y, Z через пробел:')
xyzList = list(map(int, input().split(' ')))


def isTrueStatement(xyz):
    return (not (xyz[0] or xyz[1] or xyz[2])) == (not xyz[0] and not xyz[1] and not xyz[2])


if isTrueStatement(xyzList) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")
