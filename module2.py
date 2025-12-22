#функція для вирішення суми всіх чисел від с до b кратних 3
def sol3(c, b):
    overall = 0
    for i in range(c, b + 1):
        if i % 3 == 0:
            overall += i
    return overall 

#перевірка допустимості значень c та b
def check2(c, b):
    while  c >= b:
        print('Помилка: c має бути менше b')
        c = int(input('Введіть значення с: '))
        b = int(input('Введіть значення b: '))
    return sol3(c, b)
