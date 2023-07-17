input_dict = {'lesson': 2, 'task': 21, 'course': 'python'}
# result = 'course=python&lesson=2&task=21'
input_dict = {'lesson': 2, 'course': 6}

result_list = sorted([f'{key}={value}' for key, value in input_dict.items()])
result = '&'.join(result_list)

print(result)
