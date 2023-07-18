def collatz_conjecture(n):
    result = []
    while n > 1:
        result.append(n)
        if not n % 2:
            n //= 2
        else:
            n = 3 * n + 1
    result.append(n)
    print(result)
    return result


collatz_conjecture(8)  # -> [8, 4, 2, 1]
collatz_conjecture(3)  # -> [3, 10, 5, 16, 8, 4, 2, 1]
