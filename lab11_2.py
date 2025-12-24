import pandas as pd
import matplotlib.pyplot as plt

#завантажуємо csv файл і робимо з нього датафрейм
df = pd.read_csv('myfile.csv', sep = ',',     
    parse_dates=['Date'],  
    dayfirst=False,       
    index_col='Date' )

#показуємо датафрейм
print(df)

#виводимо загальну к-сть велосипедистів за 2014 рік
df_2014= df.loc['2014']
total2014 = df_2014.sum().sum()
print('Всього велосипедистів за рік: ', total2014)

# Виводимо назви всіх доріжок (стовпців)
print(df.columns)

# Функція для підрахунку загальної кількості велосипедистів на окремій доріжці
def totaleachroad(road):
    print(f'{road}: ', df[road].sum())

# Викликаємо функцію для кожної доріжки у DataFrame
print('\n\nКількість велосипедистів на кожній доріжці: ')
for i in df.columns:
    totaleachroad(i)

# Додаємо нову колонку з місяцем для кожного рядка
df['Month'] = df.index.to_series().dt.month

# Підраховуємо загальну кількість велосипедистів по місяцях
# sum(axis=1) сумує по всіх доріжках для кожного місяця
monthly_total = df.groupby('Month').sum().sum(axis=1)

# Знаходимо місяць з максимальною кількістю людей
max_month = monthly_total.idxmax()
max_value = monthly_total.max()
print(f'Найбільше людей було у місяці {max_month}: {max_value} осіб')

# Обираємо дві доріжки для графіка
roads = ['Rachel / Papineau', 'Berri1']

# Малюємо графік динаміки велосипедистів по обраних доріжках
df[roads].plot(figsize=(15, 10))
plt.xlabel('Місяці', color='green')
plt.ylabel('Кількість велосипедистів', color='green')
plt.title('Використання двох велодоріжок у 2014 році')
plt.grid(True)
plt.show()


