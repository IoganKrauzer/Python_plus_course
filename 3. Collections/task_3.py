'''Задача 3:
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.'''

tp = (1, 2, 'st', 'fg', 4.5, 6.7, True, False)
dct = {}
for item in tp:
    if type(item) in dct:
        dct[type(item)].append(item)
    else:
        dct[type(item)] = [item]

print(dct)