# студенты курса "Аналитик данных"
da_students = {'Ivanov Alexander', 'Loginov Vladislav', 'Ershova Anna', 'Korneva Daria'}
# студенты курса "Визуализация данных"
dv_students = {'Ershova Anna', 'Egunov Andrey', 'Ignatov Alexey', 'Loginov Vladislav'}

# результат
# students = {'Loginov Vladislav', 'Ershova Anna'}

students = da_students & dv_students

print(students)
