# Пример 1
num = 7
result = "это простое число"

# Пример 2
# num = 8
# result = "это не простое число"

for div in range(2, int(num**0.5) + 1):
    if num % div == 0:
        result = "это не простое число"
        break
else:
    result = "это простое число"

print(result)

