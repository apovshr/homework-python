"""Розробити програму, яка: а) створює текстовий файл TF13_1 із символьних рядків різної довжини, 
слова в яких розділені пробілами і розділовими знаками;  б) читає вміст файла TF13_1, знаходить слова, які розпочинаються голосною літерою
і записує кожне в окремий рядок файла TF13_2; в) читає вміст файла TF13_2 і друкує його по рядках."""


#функція для відкриття файлу 
def openn (filename, mode):
    try:
        f = open(filename, mode)
    except:
        print ('File ', filename, 'wasn\'t opened :(')
        return None
    else:
        print ('File ', filename, 'was opened :)')
        return f

#два файли для роботи 
f1 = 'TF13_1.txt'
f2 = 'TF13_2.txt'

#перший файл відкрваємо для запису
f1w = openn(f1, 'w')

#якщо файл відкрився, то записуємо в нього інформацію
if f1w != None:
    for i in range(int(input('How many sentences do u want to add? '))):
        sentence = input('Write your sentence: ')
        f1w.write(sentence + '\n')
    print('File TF13_1.txt is updated!')
    f1w.close()
    print('File TF13_1.txt is closed! \n')

#перший файл тепер відкриваємо для читання, другий для запису
f1r = openn(f1, 'r')
f2w = openn (f2, 'w')

#записуємо голосні літери та пунктуацію для роботи з ними 
vowels = 'eyuioaуеїиаоєяію'
punctuation = ",.!?:;\"'()-"

#якщо обидва файли відкриті то працюємо з ними + у кінці функції усі файли закриваємо
if f1r != None and f2w != None:
    for parts in f1r: #розділяємо спочатку файл на частини, а потім по словам за пробілами, потім розділяємо по пунктуації
        for word in parts.split():
            word = word.strip(punctuation) #з функцією стріп підсказав чат джбт
            if word[0].lower() in vowels: #якщо слово починається з голосної, слово записуємо в окремий файл 
                f2w.write(word + '\n')
    f1r.close()
    f2w.close()

    print('Files are closed!\n')

#оновлений другий файл відкриваємо для читання
f2r = openn(f2, 'r')
print()

print('Updated TF13_2 file: \n')

#виводимо зміст файлу на екран
if f2r != None:
    for line in f2r.read().split():
        print(line)
    print('\nFile TF13_2.txt is closed!')
    f2r.close()


