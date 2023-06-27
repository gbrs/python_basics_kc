price_new = 89.99
price_old = 75.50
# result = 19.19

# price_new = 24
# price_old = 72
# result = 66.67

result = round(100 * abs(price_new / price_old - 1), 2)

print(result)
