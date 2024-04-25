''' Задача_2:
* В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
* Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами.
* Цифры за слова не считаем.
* Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
 Пример
На входе:
text = 'Hello world. Hello Python. Hello again.'
На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]'''

text = "Python 3.9 is the latest version of Python. It's awesome!"
# text = 'Hello world. Hello Python. Hello again.'
lst = []

for i in text:
    if i in [".", ",", ":", "!", "'"]:
        text = text.replace(i, ' ')
for k in range(len(text)):
    if text[k] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        text = text.replace(text[k], ' ')
text = text.lower().split()
print(text)

for i in set(text):
    lst.append((i, text.count(i)))
lst.sort(key=lambda a: ([1], a[0]))

print(lst[::-1])

# text = "Python 3.9 is the latest version of Python. It's awesome!"
# [('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]
# [('python', 2), ('it', 1), ('s', 1), ('the', 1), ('awesome', 1), ('of', 1), ('version', 1), ('latest', 1), ('is', 1)]
# [('version', 1), ('the', 1), ('s', 1), ('python', 2), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]
'''import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)'''
