def calculate_order_cost(dct, *args):
    cost = 0
    orders = {}
    for product in args:
        if product in dct:
            cost += dct[product]
            orders[product] = orders.setdefault(product, 0) + 1
    return cost, orders


products = {
    "ноутбук": 5000,
    "смартфон": 20000,
    "наушники": 1000,
    "монитор": 10000,
    "клавиатура": 500,
    "мышь": 200,
    "роутер": 1500,
    "принтер": 5000,
    "флешка": 1000,
    "жесткий диск": 3000
}

total_cost, orders_info = calculate_order_cost(products, 'ноутбук', 'роутер')
print(total_cost)  # 6500
print(orders_info)  # {'ноутбук': 1, 'роутер': 1}

total_cost, orders_info = calculate_order_cost(products , 'мышь', 'флешка', 'монитор', 'кабель', 'мышь')
print(total_cost)  # 11400
print(orders_info)  # {'мышь': 2, 'флешка': 1, 'монитор': 1}


