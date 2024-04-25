"""Задача 8
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

# ------------------ОПИСАНИЕ ПРОГРАММЫ------------------
# 1. Генерирует кол-во друзей
# 2. Генерирует друзей (создается список друзей, который будет потом ключами к словарю)
# 3. Генерируется кортеж из вещей (используется для создания словаря)
# 4. Создается словарь друзей + предметы


from random import randint as rnd


def random_gener():
    return rnd(3, len(name_list))


# Показать все вещи в походе
def create_list_of_all_items():
    set_dif = set()
    for key, item in persons_dict.items():
        set_dif.update(item)
    return set_dif


# Для print_dict, для отступов
def func_for_key_len(dict_):
    max_len = 0
    for key in dict_.keys():
        if len(key) > max_len:
            max_len = len(key)
    return max_len


# Вывод людей с вещами
def print_dict(dict_):
    for k, j in dict_.items():
        print(f'{k:<{func_for_key_len(dict_)}} : {j}')


# Созданию списка людей
def generate_persons_for_camping():
    keys_for_dict = []
    while len(keys_for_dict) < NUMBER_OF_PERSONS:
        helper_ = rnd(0, NUMBER_OF_PERSONS - 1)
        if name_list[helper_] not in keys_for_dict:
            keys_for_dict.append(name_list[helper_])
    return keys_for_dict


# Генерация кортежа с вещами
def generate_backpack_list():
    generate_stuff_number = rnd(2, MAX_STUFF_FOR_BACKPACK)
    person_backpack = []
    while len(person_backpack) < generate_stuff_number:
        helper_ = rnd(0, len(camping_stuff) - 1)
        if camping_stuff[helper_] not in person_backpack:
            person_backpack.append(camping_stuff[helper_])
    return tuple(person_backpack)


# Создание словаря людей с багажом
def create_persons_with_backpack():
    persons_dict_plus_staff = {}
    keys_for_dict = generate_persons_for_camping()
    for i in keys_for_dict:
        persons_dict_plus_staff[i] = generate_backpack_list()
    return persons_dict_plus_staff


# Словарь с вещами и их кол-вом--------------------------------------
def find_quantity_of_items():
    dict_1 = {}
    for key, item in persons_dict.items():
        for sub_item in item:
            if sub_item in list_of_all_items:
                dict_1[sub_item] = dict_1.get(sub_item, 0) + 1
    return dict_1


# Создается список с коль-вом вещей = 1. Уникальные вещи
def create_list_with_min_quantity_of_items():
    min_quantity_of_items = []
    for i, k in find_quantity_of_items().items():
        if k == 1:
            min_quantity_of_items.append(i)
    return min_quantity_of_items


# Создается список вещей с кол-вом NUMBER_OF_PERSONS - 1 для поиска вещи, которой нет у единственного человека
def create_list_with_max_quantity_of_items():
    max_quantity_of_items = []
    for i, k in find_quantity_of_items().items():
        if k == NUMBER_OF_PERSONS - 1:
            max_quantity_of_items.append(i)
    return max_quantity_of_items


# Список имен и вещей, которые есть у остальных, но нет у одного
def show_who_doesnt_have_an_item():
    for itm in create_list_with_max_quantity_of_items():
        for key, item in persons_dict.items():
            if itm not in item:
                print(f'{key}: {itm}')


# Вывод уникальных вещей
def show_unique_items():
    min_quantity_of_items = create_list_with_min_quantity_of_items()
    for key, item in persons_dict.items():
        for sub_item in item:
            if sub_item in min_quantity_of_items:
                print(f'{key}: {sub_item}')


camping_stuff = ['нож', 'кружка', 'приставка',
                 'кукла', 'зажигалка', 'фляжка',
                 'телефон', 'сникерс', 'ноутбук']
name_list = ['Саша', 'Валера', 'Гриша', 'Вася', 'Петя']
NUMBER_OF_PERSONS = random_gener()
MAX_STUFF_FOR_BACKPACK = 4
generate_persons_for_camping()
generate_backpack_list()
persons_dict = create_persons_with_backpack()
# persons_dict = {'Вася': ('сникерс', 'нож', 'приставка', 'кружка', 'девушка'),
#                 'Валера': ('сникерс', 'нож', 'приставка', 'кружка'),
#                 'Саша': ('сникерс', 'кружка', 'нож', 'приставка', 'девушка')}
print('---------------------')
print('Друзья взяли с собой:')
print('---------------------')
print_dict(persons_dict)
print('---------------------')
print('Общие вещи:')
print('---------------------')
list_of_all_items = create_list_of_all_items()
print(', '.join(list_of_all_items))
print('---------------------')
print('Уникальные вещи: ')
print('---------------------')
show_unique_items()
print('---------------------')
print('Есть у всех, кроме: ')
print('---------------------')
show_who_doesnt_have_an_item()
