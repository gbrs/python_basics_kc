n = 54412
# result = [False, False, True, False, True]


# result = [not bool(n[i + 1] % n[i]) for i in range(len(n) - 1)]
# result.insert(0, False)

n = [int(figure) for figure in list(str(n))]
result = [False]
for i in range(len(n) - 1):
    if n[i] == 0:
        result.append(False)
    elif n[i + 1] % n[i] == 0:
        result.append(True)
    else:
        result.append(False)

print(result)
