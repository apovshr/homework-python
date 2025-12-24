import json
import matplotlib.pyplot as plt
import numpy as np

#відкриваємо файл джейсон для читання
with open('jsonfile.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

#рахуємо загальну кількість учнів по кожному з закладів
schools_total = sum(students['школа'])
technicums_total = sum(students['технікум'])
colleges_total = sum(students['училище'])

# Створюємо фігуру та осі
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))

# Дані для діаграми
institution_types = ["Школи", "Технікуми", "Училища"]
data = [schools_total, technicums_total, colleges_total]
colors = ['pink', 'blue', 'green']

# Функція для форматування тексту на секторах
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} учнів)"

# Створюємо кругову діаграму
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  colors=colors,
                                  textprops=dict(color="w"),
                                  startangle=90,
                                  explode=(0.05, 0.05, 0.05))

# Додаємо легенду
ax.legend(wedges, institution_types,
          title="Типи закладів",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=10)

# Налаштування тексту на секторах
plt.setp(autotexts, size=10, weight="bold")

# Загальна кількість
total_students = sum(data)
ax.set_title(f"Розподіл учнів по навчальних закладах\nЗагальна кількість: {total_students} учнів", 
             fontsize=13, fontweight='bold', pad=20)


plt.show()
