# def func_for_key_len(dict_):
#     max_len = 0
#     for key in dict_.keys():
#         if len(key) > max_len:
#             max_len = len(key)
#     return max_len
#
#
# def print_dict(dict_):
#     for k, j in dict_.items():
#         print(f'{k:<{func_for_key_len(dict_)}} : {j}')
#
#
# # persons_dict = {'Андур': ('сникерс', 'нож', 'приставка', 'кружка'),
# #                 'Валера': ('девушка', 'телефон', 'сникерс', 'зажигалка'),
# #                 'Борда': ('телефон', 'кружка', 'приставка', 'нож')}
# #
# # s_1 = ('сникерс', 'нож', 'приставка', 'кружка')
# # s_2 = ('девушка', 'телефон', 'сникерс', 'зажигалка')
# # s_3 = ('телефон', 'кружка', 'приставка', 'нож')
#
# persons_dict = {'Андур': ('сникерс', 'нож', 'приставка', 'кружка', 'девушка'),
#                 'Валера': ('сникерс', 'нож', 'приставка', 'кружка'),
#                 'Борда': ('сникерс', 'нож', 'кружка')}
#
# s_1 = ('сникерс', 'нож', 'приставка', 'кружка', 'девушка')
# s_2 = ('сникерс', 'нож', 'приставка', 'кружка')
# s_3 = ('сникерс', 'нож', 'кружка')
#
# # Нет зажигалки
# NUMBER_OF_PERSONS = 3
# print_dict(persons_dict)
# set_all_items = set()
# set_all_items.update(set(s_1))
# set_all_items.update(set(s_2))
# set_all_items.update(set(s_3))
# print()
# print(set_all_items)
#
# dict_1 = {}
# for key, item in persons_dict.items():
#     for k in item:
#         if k in set_all_items:
#             dict_1[k] = dict_1.get(k, 0) + 1
# print()
# for i, k in dict_1.items():
#     print(f'Slovar {i} : {k}')
# print()
#
# min_ = []
# for i, k in dict_1.items():
#     if k == 1:
#         min_.append(i)
# print(min_)
#
# for i, k in persons_dict.items():
#     for n in k:
#         if n in min_:
#             print(f'Check 1 {i}: {n}')
#
# max_ = []
# for i, k in dict_1.items():
#     if k == NUMBER_OF_PERSONS - 1:
#         max_.append(i)
#
# print(f'Список макс вещей {max_}')
#
# for itm in max_:
#     for key, item in persons_dict.items():
#         if itm not in item:
#             print(f'Check 2 {key}: {itm}')
#
# '''
#      {'Андур': ('сникерс', 'нож', 'приставка', 'кружка', 'девушка'),
#      'Валера': ('сникерс', 'нож', 'приставка', 'кружка'),
#      'Борда': ('сникерс', 'нож', 'кружка')}'''
