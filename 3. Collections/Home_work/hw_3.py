'''Задача_3
Дан список повторяющихся элементов lst.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.'''

lst = [1, 2, 3, 4, 5]
ls = []

for i in set(lst):
    if lst.count(i) > 1:
        ls.append(i)

print(ls)

# duplicates = set()
#
# for item in lst:
#     if lst.count(item) >= 2:
#         duplicates.add(item)
#
# result = list(duplicates)
# print(result)
