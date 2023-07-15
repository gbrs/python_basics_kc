number = 4096 # число для теста

is_two_power = False
if number > 0:
    while number % 2 == 0:
        number = number / 2
    if number == 1:
        is_two_power = True

print(is_two_power)
