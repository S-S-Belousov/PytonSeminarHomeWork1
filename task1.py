# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def getDay(numDay):
    return {
        numDay == 1: 'рабочий день',
        numDay == 2: 'рабочий день',
        numDay == 3: 'рабочий день',
        numDay == 4: 'рабочий день',
        numDay == 5: 'рабочий день',
        numDay == 6: 'выходной день',
        numDay == 7: 'выходной день'
    }[True]


day = int(input('Введите день недели: '))
if 1 <= day <= 7:
    print(f'Это {getDay(day)}')
else:
    print('Введен не корректный день недели')