my_string = 'zis jqd qbdx qjjgsd bcd zjm fbc bvbx'
secret_dict = {
    'v': 'w',
    'x': 'y',
    'i': 'h',
    'q': 'l',
    'c': 'n',
    'b': 'a',
    'f': 'r',
    'j': 'o',
    's': 'e',
    'z': 't',
    'g': 'k'}

decrypted_list = []

for char in my_string:
    if char in secret_dict:
        decrypted_list.append(secret_dict[char])
    else:
        decrypted_list.append(char)

decrypted_string = ''.join(decrypted_list)

print(decrypted_string)
