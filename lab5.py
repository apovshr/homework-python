# Створюємо словник навчальних закладів з 5 записами
schools = {
    1: {'тип': 'школа', 'учні': 120, 'місто': 'Київ'},
    2: {'тип': 'технікум', 'учні': 80, 'місто': 'Львів'},
    3: {'тип': 'училище', 'учні': 60, 'місто': 'Одеса'},
    4: {'тип': 'школа', 'учні': 150, 'місто': 'Харків'},
    5: {'тип': 'школа', 'учні': 100, 'місто': 'Дніпро'},
}

#меню для вибору задачі
def show_menu():
    print("\nМеню:")
    print("1 - Переглянути всі записи")
    print("2 - Додати новий запис")
    print("3 - Змінити існуючий запис")
    print("4 - Видалити запис")
    print("5 - Порахувати загальну кількість учнів у школах")
    print("0 - Вихід")

#функція while, яка буде виконувати вибрану задачу
while True:
    show_menu()
    choice = input("Оберіть дію: ")
    
    #задача вивести усі дані
    if choice == '1':
        print("\nВсі записи:")
        for key, value in schools.items():
            print(f"{key}: {value}")
    
    #задача додати новий запис
    elif choice == '2':
        try:
            new_id = int(input("Введіть новий ID запису: "))
            if new_id in schools:
                print("Запис з таким ID вже існує!")
                continue
            typ = input("Тип закладу (школа/технікум/училище): ")
            pupils = int(input("Кількість учнів: "))
            city = input("Місто: ")
            schools[new_id] = {'тип': typ, 'учні': pupils, 'місто': city}
            print("Запис додано.")
        except ValueError:
            print("Помилка: некоректне введення числа.")
    
    #задача змінити існуючий запис
    elif choice == '3':
        try:
            edit_id = int(input("Введіть ID запису для зміни: "))
            if edit_id not in schools:
                print("Запис з таким ID не знайдено!")
                continue
            typ = input("Новий тип закладу: ")
            pupils = int(input("Нова кількість учнів: "))
            city = input("Нове місто: ")
            schools[edit_id] = {'тип': typ, 'учні': pupils, 'місто': city}
            print("Запис змінено.")
        except ValueError:
            print("Помилка: некоректне введення числа.")
    
    #видалення запису
    elif choice == '4':
        try:
            del_id = int(input("Введіть ID запису для видалення: "))
            if del_id in schools:
                del schools[del_id]
                print("Запис видалено.")
            else:
                print("Запис з таким ID не існує!")
        except ValueError:
            print("Помилка: некоректне введення числа.")
    
    #загальна к-сть учнів у школах
    elif choice == '5':
        total = 0
        for record in schools.values():
            if record['тип'] == 'школа':
                total += record['учні']
        print(f"Загальна кількість учнів у школах: {total}")
    
    #вихід
    elif choice == '0':
        print("Вихід з програми.")
        break
    else:
        print("Помилка. Спробуйте ще раз.")
