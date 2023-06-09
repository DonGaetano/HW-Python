# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

list_phrase = input('Введите текст кричалки Винни-Пуха: ').split()

list_vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']

list_phrase_vowels = []
for i in range (len(list_phrase)):
    list_phrase_vowels.append(list(filter(lambda x: x in list_vowels, list_phrase[i])))

list_count = list(map(lambda x: True if len(x) == len(list_phrase_vowels[0]) else False, list_phrase_vowels))

if sum(list_count) == len(list_count):
    print('Парам пам-пам') 
else: 
    print('Пам парам')
