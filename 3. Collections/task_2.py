'''Задача 2:
✔Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях'''

value = input('Введите данные: ')

try:
    if not value.isdigit():
        value = float(value)
    elif value.isdigit() and int(value) > 0:
        value = int(value)
except:
    if not value.islower():
        value = value.upper()
    else:
        value = value.lower()

print(value)
print(type(value))