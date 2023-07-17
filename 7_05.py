# Пример 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = True

# Пример 2
# a = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# result = False

# Пример 3
# a = [1, 2, 3, 4]
# result = False

result = sum([1 if x % 2 else -1 for x in a]) > 0

print(result)
