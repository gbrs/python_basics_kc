card = '5468350018455833'
# result = '************5833'

result = '*' * (len(card) - 4) + card[-4:]

print(result)
