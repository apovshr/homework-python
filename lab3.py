#Отримати кожний 4-й символ починаючи від 19-го символа і до кінця.

sentence = input('Enter your sentence (more than 19 symbols): ')

#перевірка чи справді у реченні 19 симболів
while len (sentence) < 19:
    print ('Error! The sentence has less than 19 symbols.')
    sentence = input('Enter new sentence: ')

#виписуємо нове речення, яке починається з 19 і йде до кінця з кроком 4
print ('Your new sentence: ', sentence [19::4])


#З'ясувати, чи правильно, що в заданому слові є усі букви, що входять в запропоноване користувачем слово.

main_word = input('\n\nEnter your main word: ').lower()
word = input('Enter a word for checking: ').lower()

all_same = True #буде рахувати чи всі літери у слові входять у слово, запропоноване користувачем
 
#функція для перевірки літер
for letter in word:
    if letter not in main_word:
        all_same = False
        break 
    
#виведення результатів
if all_same == True:
    print ('All letters are found in a word')
else:
    print ('Not all letters are found in your word') 


#Задано речення. Скласти програму, яка визначає і виводить на екран його найдовше слово (прийняти, що таке слово є одним).

#функція, яка просить речення, розділяє по словам, розраховує довжину слів та виводить найдовше слово і його довжину
def calculations():
    while True:
        sen = input('\n\nEnter your sentence: ')
        words = sen.split(' ')
        print('Words in a sentence:', words)

        max_len = 0
        longestw = ''
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
                longestw = word

        count = 0
        for word in words:
            if len(word) == max_len:
                count += 1

        if count > 1:
            print('Error! More than one word has the same maximum length. Try again.\n')
            continue  # просимо ввести речення ще раз
        else:
            print('The longest word ', longestw,  'has length:', max_len)
            break  # вихід з циклу


calculations()
