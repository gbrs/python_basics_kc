# Пример 1
nums = [40, 16, 8, 17, 15]
result = [16, 17]
# пара 16 и 15 не подходит, так как сумма 16 и 17 больше

# Пример 2
# nums = [0, 2, 35, 42, 45, 14, -6, -1]
# result = [-1, 0]





nums.sort()

result = [nums[0], nums[-1]]
mn = nums[-1] - nums[0]
for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] <= mn:
        mn = nums[i] - nums[i - 1]
        result = [nums[i - 1], nums[i]]

print(result)
