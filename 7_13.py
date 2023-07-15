students = {'Бабаков': 80, 'Волгов': 100, 'Антонов': 99}
# students_order = [(1, 'Антонов'), (2, 'Волгов')]

students_list = [name for name, score in students.items() if score >= 90]
students_list.sort()
students_order = [(i, name) for i, name in enumerate(students_list, start=1)]

print(students_order)