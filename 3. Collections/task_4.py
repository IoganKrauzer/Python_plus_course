'''Задача 4:
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.'''

sample_list = [1, 2, 1, 1, 2]

for item in set(sample_list):
    if sample_list.count(item) == 2:
        sample_list.remove(item)
        sample_list.remove(item)
print(sample_list)

# sample_list = [1,2,1,1,2]
#
# for item in sample_list:
#     if sample_list.count(item) == 2:
#         sample_list.remove(item)
#         sample_list.remove(item)
# print(sample_list)

