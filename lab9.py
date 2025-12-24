"""Знайти дані Population, total для уcіх країн світу за 2019 рік. 
Вивести вміст .csv файлу на екран. Організувати пошук даних для введених 
користувачем назв країн та записати результат пошуку у новий .csv файл."""

import csv
import os

#відкриваємо csv файл та читаємо дані, виводимо їх користувачу, потім закриваємо файл (якщо все працює правильно, інакше видаємо помилку)
try:
    csvfile = open('/Users/nastyalytvynenko/test/Python hw/lab 9/myfile.csv', 'r')
    reader = csv.DictReader(csvfile, delimiter = ',') #відкрили файл
    print('Population, total : 2019 year\n\n')
    for row in reader:
        print(row['Country Name'], ': ', row['2019']) #вивели на екран дані з файлу
    csvfile.close() #закрили файл
except Exception as e:
    print('Error with opening myfile.csv: ', e) 

print('\n\n')

#відкриваємо знову csv файл для читання та даємо змогу користувачу шукати по країнам і заносити результати у новий csv файл (якщо програма не буде працювати, то видасть помилку)
try:
    csvfile = open('/Users/nastyalytvynenko/test/Python hw/lab 9/myfile.csv', 'r')
    reader = csv.DictReader(csvfile, delimiter = ',') #беремо дані з csv файлу (словники)
    data = list(reader) #список словників (дані про країни), де кожен словник це окремий рядок у csv файлі
    countryname = [row['Country Name'] for row in data]
    for i in range(int(input('How many countries do u want to add to new file?: '))):
        country = input('Enter name of a country: ')
        while country.lower() not in [c.lower() for c in countryname]:
            country = input('Error with name of a country, please enter again: ')

        for row in data:
            if country.lower() == row['Country Name'].lower(): #все робимо маленькими літерами, щоб порівнювати назви країн без помилок
                print(row['Country Name'], ': ', row['2019'])
                with open('/Users/nastyalytvynenko/test/Python hw/lab 9/Updated_myfile.csv', 'a') as f:
                    writer = csv.writer(f, delimiter = ',') 
                    writer.writerow([row['Country Name'], row['2019']]) #записуємо дані про обрані країни у новий csv файл
                    print(row['Country Name'], ' was added to new file\n')
    csvfile.close()
except:
    print('Program is not working')
