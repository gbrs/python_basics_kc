str_1 = 'AaB'
str_2 = 'Ab'
# is_the_same_letters = True
#
# str_1 = 'Aa'
# str_2 = 'AaB'
# is_the_same_letters = False

is_the_same_letters = set(str_1.lower()) == set(str_2.lower())

print(is_the_same_letters)
