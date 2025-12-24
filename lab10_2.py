import csv
import matplotlib.pyplot as plt 
import numpy as np

#вказую роки, а також роблю два пустих списка для населення україни та британії
years = list(range(2008, 2025))
populationu = []
populationb = []

#функція, яка зі всього файлу буде брати інформацію тільки по населенню україни та британії
try:
    with open('population.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        
        for row in reader:
            if row['Country Name'] == 'Ukraine':
                populationu = [int(row[str(year)]) for year in years]
            elif row['Country Name'] == 'United Kingdom':
                populationb = [int(row[str(year)]) for year in years]
    
    print("Роки:", years)
    print("Україна:", populationu)
    print("Великобританія:", populationb)

except Exception as e:
    print('Mistake:', e)

#вказуємо за що будуть відповідати вісі
x = years
y = populationu
z = populationb

#малюємо граф
plt.plot(x, y, label = 'Ukraine', color = 'blue')
plt.plot(x, z, label = 'United Kingdom', color = 'yellow')
plt.xlabel('Years', color = 'green')
plt.ylabel('Population (millions)', color = 'green')
plt.legend()
plt.title('Population graph')
plt.grid(True)
plt.show()

#Стовпчаста діаграма для однієї країни
def plot_bar_chart():
    while True:
        country_name = input("Введіть номер країни для стовпчастої діаграми (Ukraine - 1 або United Kingdom - 2): ")
        
        if country_name == '1':
            data = populationu
            country_label = 'Ukraine'
            break
        elif country_name == '2':
            data = populationb
            country_label = 'United Kingdom'
            break
        else:
            print("Країна не знайдена. Спробуйте ще раз.")
    
    plt.bar(x, data, color='skyblue')
    plt.xlabel('Years')
    plt.ylabel('Population (millions)')
    plt.title(f'Population of {country_label} by year')
    plt.xticks(x, rotation=45)
    plt.grid(axis='y')
    plt.show()

# Виклик функції
plot_bar_chart()
