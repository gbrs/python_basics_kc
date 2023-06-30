'''a = [1, 2, 2, 1, 3, 2, 3]
b = 1
# -> a = [2, 2, 3, 2, 3]'''

a = [1, 2, 2, 1, 3, 2, 3]
b = 2 
# -> a = [1, 2, 1, 3, 3]

a.remove(b)
a.reverse()
a.remove(b)
a.reverse()

print(a)
