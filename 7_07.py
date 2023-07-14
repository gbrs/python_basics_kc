lst_1 = ["1", "0", "0", "1"]
lst_2 = ["0", "1", "1", "0"]
result = True

# lst_1 = ["1", "0", "0", "1"]
# lst_2 = ["0", "1", "1", "1"]
# result = False

result = all([i != j for i, j in zip(lst_1, lst_2)])

print(result)
