# str_1 = "привет"
# str_2 = "провал"
# result = False

# str_1 = "кот"
# str_2 = "ток"
# result = True

str_1 = "кот"
str_2 = "тко"


# result = str_1 == str_2[::-1]
result = sorted(str_1) == sorted(str_2)

print(result)
