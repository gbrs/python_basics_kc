'''
# ->
list_1 = [1, 3, 5]
list_2 = [8, 2]
list_3 = [1, 2, 3, 5, 8]
list_3_len = 5'''


list_1 = [1, 5, 3]
list_2 = [2, 8]

list_1.sort()
list_2.sort(reverse=True)

list_3 = list_1[:]
list_3.extend(list_2)
list_3_len = len(list_3)
list_3.sort()

print(list_1, list_2, list_3, list_3_len)
