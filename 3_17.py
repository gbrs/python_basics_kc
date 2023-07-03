a = [1, 6, 4, 3]

sum_left = sum(a[:len(a) // 2])
sum_right = sum(a[len(a) // 2:])
result = sum_left == sum_right

print(result)
