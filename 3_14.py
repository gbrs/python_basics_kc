# my_set = {0, 10, 100}
# to_delete = 0
# ====>
# my_set = {10, 100} # удалили 0

my_set = {0, 10, 100}
to_delete = -2
# ====>
# my_set = {0, 10, 100} # ничего не сделали

if to_delete in my_set:
    my_set.remove(to_delete)

print(my_set)

