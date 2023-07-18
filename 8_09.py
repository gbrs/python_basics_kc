def reverse_tuple(lst):
    result = []
    for val in lst[::-1]:
        if val not in result:
            result.append(val)
    return tuple(result)


reverse_tuple([1, 3, 4])  # -> (4, 3, 1)
reverse_tuple([1, 3, 4, 4, 5, 2])  # -> (2, 5, 4, 3, 1)
reverse_tuple([1, 2, 4, 6])
