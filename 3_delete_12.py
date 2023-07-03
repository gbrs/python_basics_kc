menu = {'White Chocolate Mocha', 'Americano', 'Flat White', 'Latte',
        'Blueberry Muffin', 'Chocolate Chip Cookie'}
stop = {'White Chocolate Mocha', 'Blueberry Muffin'}

menu_today = menu.difference(stop)

# menu_today = {'Americano', 'Flat White', 'Latte', 'Chocolate Chip Cookie'}

print(menu_today)
