#Дано одномірний масив, що складається з N цілочисельних елементів. Масив користувач має ввести з клавіатури. Знайти максимальний додатний елемент.

#пустий масив для заповнення
list1 = []

#задаємо розмір масиву
print('Enter n value: ', end='')
n = int(input())

#перевірка, щоб розмір масиву не був 0
while n < 1:
      n = int(input('Error! n can not be less than 1, please enter new n: '))

#заповнюємо пустий масив елементами
for i in range(n):
   list1.append(int(input(f'Enter element {i}: ')))
print('\nYour list: ', list1)

maxi = [x for x in list1 if x > 0]

if maxi:
   print('\nMaximum positive element is: ', max(maxi))
else:
   print('There are no positive numbers')
print('\n')


#Заповнити двовимірний масив розміром 7x7 таким чином, як показано на рисунку згідно з Вашим варіантом. Вивести масив на екран. Для виконання завдання використовуйте цикли.

print('Making an array\n\n')
n = 7
list2 = [[0]*n for i in range(n)] #створює n елементів в n рядках (за кількість рядків відповідає функція for)

#розрахунок масиву
for i in range(n):
   for j in range(n-1, -1, -1):
      if n > j+i:
         list2[i][j] = (1 + j + i )
      else:
         list2[i][j] = 0

#друкуємо масив
for row in list2:
   print(*row)
print('\n')


#Видалення всіх елементів з парним порядковим номером.

#пустий масив
list3 = []

#заповнюємо масив елементами
for i in range (int(input('Enter how many elements will be on the list: '))):
   list3.append(int(input('Enter an element: ')))

print('Ваш масив: ', list3)

#записуємо елемент, якщо число парне за порядком
list3 = [list3[i] for i in range(len(list3)) if i % 2 != 0]

#друкуємо результат
print('Новий масив: ', list3)
print('\n')


#Перестановка елементів списку у зворотньому порядку.

#задаємо пустий список
list4 = []

#заповнюємо список
for i in range(int(input('Enter how many elemets will be on the list: '))):
   print('Enter new element: ', end='')
   list4.append(int(input()))

#друкуємо початковий список
print('Initial list: ', end='')
for r in range(len(list4)):
   print(f'{list4[r]} ', end= '')
print ()

#друкуємо список у зворотньому порядку
print('Reverse list: ', end='')
list4.reverse()
for r in range(len(list4)):
   print(f'{list4[r]} ', end= '')
print('\n')

#Задано текст з малих латинських літер. Скласти програму, яка формує множину з літер, що входять у цей текст, та визначає кількість розділових знаків у тексті.

#просимо записати речення
list5 = input('Enter your sentence: ')

#пустий список для зазначення усіх літер у реченні
finallist = []

#функція для перебору символів й зберігання тільки літер у новий список
for i in list5:
   if i.isalpha(): 
      finallist.append(i)

#робимо так, щоб у новий список літери зберігалися без повторень
finallist = set(finallist)

#зазначаємо усю пунктуацію для вираховування кількості у реченні
punctuation = '.,;:!?-()\"\''

num = sum(list5.count(c) for c in punctuation)

#виведеня результатів. перший результат це кількість розділових знаків, другий це множина літер
print('Number of punctuation in text: ', num)
print('Letters: ', finallist)


