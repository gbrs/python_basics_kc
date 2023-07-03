student = {"name": "Igor", "notes": [4, 5, 4]}
# result = {"name": "Igor", "max_note": 5}

result = student.copy()
result['max_note'] = max(result['notes'])
result.pop('notes')

print(result)
