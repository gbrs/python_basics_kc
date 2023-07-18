def calculator(op, a, b):
    if op == '+':
       return a + b
    if op == '-':
       return a - b
    if op == '^':
       return a**b
    if op == '*':
       return a * b
    if op == '/' and b != 0:
       return a / b
    return 'Error'



print(calculator('+', 2, 4))  # -> 6
print(calculator('^', 2, 4))  # -> 16
print(calculator('', 2, 4))  # -> 'Error'


