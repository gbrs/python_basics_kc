def sorting_hat(new_students):
    department_traits = {
        'Гриффиндор': ['храбрость', 'благородство', 'честь'],
        'Пуффендуй': ['трудолюбие', 'верность', 'честность'],
        'Когтевран': ['ум', 'любознательность', 'творчество'],
        'Слизерин': ['хитрость', 'амбициозность', 'находчивость']}
    departments = {department: 0 for department in department_traits}
    trait_department = {}
    for department in department_traits:
        for trait in department_traits[department]:
            trait_department[trait] = department
    sorted_students = {}

    for name, trait in new_students.items():
        department = trait_department[trait]
        sorted_students[name] = department
        departments[department] += 1

    return sorted_students, departments

new_students = {'Сириус Блэк': 'храбрость', 'Аманда Коршун': 'любознательность',
                'Пенелопа Вулпинголд': 'находчивость', 'Артур Поттер': 'храбрость', 'Тесая Блэк': 'ум'}
sorted_students, departments = sorting_hat(new_students)  # ->
# sorted_students = {'Артур Поттер': 'Гриффиндор', 'Сириус Блэк': 'Гриффиндор', 'Аманда Коршун': 'Когтевран',
#                    'Тесая Блэк': 'Когтевран', 'Пенелопа Вулпинголд': 'Слизерин'}
# departments = {'Гриффиндор': 2, 'Когтевран': 2, 'Пуффендуй': 0, 'Слизерин': 1}

print(sorted_students)
print(departments)


