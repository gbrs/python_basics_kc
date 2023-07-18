def update_tuple(input_tuple, el_del):
    result = list(input_tuple)
    if el_del in result:
        result.remove(el_del)
    return tuple(result)


update_tuple((1, 2, 3), 1)  #-> (2, 3)
update_tuple((1, 2, 3, 3, 9, 5), 3)  #-> (1, 2, 3, 9, 5)
update_tuple((1, 2, 3), 9)  #-> (1, 2, 3)