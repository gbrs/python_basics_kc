anton_courses = {'SimulatorAnalyst': 56,
                 'StartML': 87,
                 'DataAnalyst': 140}
# ->
# anton_courses = {'SimulatorAnalyst': 56,
#                  'StartML': 87,
#                  'DataAnalyst': 140,
#                  'HardML': 120}
# courses = ['SimulatorAnalyst', 'StartML', 'DataAnalyst', 'HardML']
# StartML = 87

anton_courses['HardML'] = 120
courses = list(anton_courses.keys())
StartML = anton_courses['StartML']

print(anton_courses, courses, StartML)
