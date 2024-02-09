order = input('Введите список слов: ')
word = input('Введите слова для проверки: ')
word.split(',')
if word in order:
    print('True')
else:
    print('False')

