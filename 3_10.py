'''
В переменной numbers_list сохранен список с целыми числами. В списке минимум два разных целых числа.
В переменную numbers_list_ordered сохраните все числа из списка numbers_list, отсортированные по убыванию.
При этом сам список numbers_list не должен изменяться.
В переменную numbers_set сохраните множество из уникальных чисел из списка numbers_list.
Дополните это множество следующим целым числом после максимального числа из numbers_list.
В переменную numbers_frozenset сохраните неизменяемое множество из всех уникальных чисел из списка numbers_list,
кроме минимального числа.
'''


# Пример 1
# numbers_list = [1, 5, 3, 3, 5]
#
# numbers_list_ordered = [5, 5, 3, 3, 1]
# numbers_set = set([1, 3, 5, 6])
# numbers_frozenset = frozenset([3, 5])


# Пример 2
# numbers_list = [-1, 0, 1]
#
# numbers_list_ordered = [1, 0, -1]
# numbers_set = set([-1, 0, 1, 2])
# numbers_frozenset = frozenset([0, 1])

# Пример 3
numbers_list = [-1, -5, -1]

# numbers_list_ordered = [-1, -1, -5]
# numbers_set = set([-5, -1, -2])
# numbers_frozenset = frozenset([-1])

numbers_list_ordered = sorted(numbers_list, reverse=True)
numbers_set = numbers_list[:]
numbers_set.append(numbers_list_ordered[0] + 1)
numbers_set = set(numbers_set)
numbers_frozenset = set(numbers_list[:])
numbers_frozenset.remove(numbers_list_ordered[-1])
numbers_frozenset = frozenset(numbers_frozenset)

print(numbers_list, numbers_list_ordered, numbers_set, numbers_frozenset)
