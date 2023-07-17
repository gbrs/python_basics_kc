# Пример 1
# coffee = 0.1
# milk = 1
# visitors = 14

# Пример 2
# coffee = 0.07
# milk = 0.1
# visitors = 4

coffee = 1
milk = 2

coffee *= 1000
milk *= 1000

visitors = 0

while True:
    if (visitors + 1) % 3 == 0:
        if coffee >= 7 and milk >= 100:
            visitors += 1
            coffee -= 7
            milk -= 100
        else:
            break
    elif (visitors + 1) % 5 == 0:
        if coffee >= 7 and milk >= 180:
            visitors += 1
            coffee -= 7
            milk -= 180
        else:
            break
    else:
        if coffee >= 7:
            visitors += 1
            coffee -= 7
        else:
            break
    print(milk, coffee)

print(visitors)
