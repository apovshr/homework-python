"""Задано дані про кількість учнів у кожному з n=6 навчальних закладів і про тип закладів (школа, технікум або училище). 
Скласти програму, яка визначає загальну кількість учнів шкіл."""

import json

# Створюємо словник з трьома типами закладів, поки в них всі 0 учнів
students = {
    'школа': [0, 0], 
    'технікум': [0, 0], 
    'училище': [0, 0]
}

# Відкрили файл для запису початкових даних
with open('jsonfile.json', 'w', encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False)


# Функція для додавання учнів у заклади
def addi(typee, e, addition):
    if typee == 1:
        students['школа'][e] += addition
    elif typee == 2:
        students['технікум'][e] += addition
    elif typee == 3:
        students['училище'][e] += addition

    print('\nУчні додані!!\n')

    # Записуємо оновлений словник у файл
    with open('jsonfile.json', 'w', encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False)


# Головне меню зі всіма діями
while True:
    choice = int(input('''Введіть варіант дії, яку ви хочете здійснити: 
                    1 - Додати кількість учнів у навчальний заклад,
                    2 - Подивитися скільки всього учнів у навчальних закладах,
                    3 - Подивитися скільки всього учнів у школах, 
                    4 - Вихід\n'''))
    
    if choice == 1:
        typee = int(input('Оберіть тип закладу: 1 - Школа, 2 - Технікум, 3 - Училище: '))
        while typee not in [1, 2, 3]:
            typee = int(input('Помилка! Ви обрали неправильний тип закладу, спробуйте ще раз (1 - Школа, 2 - Технікум, 3 - Училище): '))
        
        e = int(input('Оберіть номер навчального закладу (1 чи 2): ')) - 1
        while e not in [0, 1]:
            e = int(input('Помилка! Ви обрали неправильний номер закладу, спробуйте ще раз (1 чи 2) : ')) - 1
        
        addition = int(input('Введіть кількість учнів: '))
        addi(typee, e, addition)
    
    elif choice == 2:
        # Читаємо файл лише для перегляду, не змінюємо основний словник
        with open('jsonfile.json', 'r', encoding='utf-8') as f:
            temp_data = json.load(f)
            for key, values in temp_data.items():
                print(key, ': ', values)
    
    elif choice == 3:
        overall = students['школа'][0] + students['школа'][1]
        print('Всього учнів у школах: ', overall)
    
    elif choice == 4:
        print('Завершення програми...')
        break
