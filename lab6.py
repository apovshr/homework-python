#шаблон для заповнювання словника
template = {
    'Група': '',
    'ПІБ': '',
    'Курс': 0,
    'Предмет': '',
    'Оцінка': 0
}

#це буде основний словник, який буде мати структуру шаблону
students = []

#функція для додавання інформації по учнях
def adding(template, students):
    for i in range(int(input('Кількість студентів: '))):
        print('\nДані студента номер ', i + 1, ': \n')
        student = template.copy() #копіюємо шаблон для заповнення 

        student['Група'] = input('Введіть групу студента: ')
        student['ПІБ'] = input('Введіть прізвище, ім\'я та по-батькові студента: ')
        student['Курс'] = int(input('Введіть курс студента: '))
        student['Предмет'] = input('Введіть назву предмету: ')
        student['Оцінка'] = int(input('Введіть оцінку: '))

        students.append(student)
        print('Студента', i + 1, 'додано успішно! \n')
        print()

    main_menu(template, students)

#функція виведення усіх учнів на екран      
def printing(students):
    for i in range(len(students)):
        print()
        print (f'Студент {i + 1}: ')
        for key in students[i]:
            print(f'{key}: {students[i][key]}')
    main_menu(template, students)

#функція для видалення конкретного учня
def delete(index, students):
    if 0 <= index < len(students):
        del students [index]
        print('Студент видалений')
    else:
        print('Помилка, немає студента під таким номером')
    main_menu(template, students)

#функція для оновлення інформації про конкретного учня 
def updating(index, key, students):
   
    if 0 <= index < len(students):
        new = input((f'Введіть нове значення {key} : '))
        students [index][key] = new
        print(f'Оновлена інформація про {key} : {new}')
    else:
        print('Помилка, студента під таким номером не знайдено')
    main_menu(template, students)

#головне меню, яке буде питати, яку дію виконати та викликати потрібну функцію
def main_menu (template, students):
    while True:
        n = int(input(('\nОберіть дію: \n1) Додати учня (введіть \'1\') \n2) Вивести усіх учнів на екран (введіть \'2\')\n3) Видалити конкретного учня (введіть (введіть \'3\') \
                 \n4) Оновити значення про вже доданого учня (введіть \'4\') \n5) Вихід (введіть \'5\')\n')))
        print()
    
        match n:
            case 1:
                adding (template, students)
            case 2:
                printing(students)
            case 3:
                delete(int(input('Введіть номер учня для видалення: ')) - 1, students)
            case 4:
                i = int(input('Введіть номер студента: ')) - 1
                key = int(input('Введіть номер поля для оновлення (1 - Група, 2 - ПІБ, 3 - Курс, 4 - Предмет, 5 - Оцінка): '))
                updating(i, keydetect(key), students)
            case 5:
                print('Завершення програми...')
                break

#функція для вичеслення, з яким саме полем користувач хоче взаємодіяти (допомагає уникнути помилок при вводі поля)
def keydetect(key):
    match key:
        case 1:
            return 'Група'
        case 2:
            return 'ПІБ'
        case 3:
            return 'Курс'
        case 4:
            return 'Предмет'
        case 5:
            return 'Оцінка'

#перша за викликом функія - меню
main_menu (template, students)
              
