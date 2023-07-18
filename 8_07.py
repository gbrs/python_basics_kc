input_list = [('Anna', 13), ('Ivan', 20), ('Irina', 23), ('Olga', 25),
              ('Ivan', 30), ('Oleg', 24), ('Olga', 26)]
# result = [('Ivan', 30), ('Olga', 25), ('Ivan', 20)]

result = list(
            filter(
                lambda x: not x[1] % 5,
                sorted(input_list, key=lambda x: -x[1])
            )
        )

print(result)
