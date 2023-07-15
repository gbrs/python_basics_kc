# Пример 1
m = [[1, 23, 4],
     [3, 2, 1],
     [6, 3, 4]]
result = False

# Пример 2
# m = [[1, 23, 4],
#      [3, 2, 1],
#      [1, 3, 4]]
# result = True

sm1 = sm2 = 0
length = len(m)
for i in range(length):
    sm1 += m[i][i]
    sm2 += m[i][length - i - 1]

result = sm1 == sm2

print(result)
