import csv

cart = []

def add_sandwich(sandwich):
    cart.append({'type': 'sandwich', 'name': sandwich})

def add_drink(drink):
    cart.append({'type': 'drink', 'name': drink})

def add_meal(sandwich, size, drink):
    cart.append({'type': 'meal', 'sandwich': sandwich, 'size': size, 'drink': drink})

def clear_cart():
    cart.clear()

def get_invoice():
    total = 0
    rows = []
    rows.append(['Item', 'Price (USD)'])
    rows.append(['-'*20, '-'*10])
    for item in cart:
        if item['type'] == 'sandwich':
            rows.append([item['name'], '3.99'])
            total += 3.99
        elif item['type'] == 'drink':
            rows.append([item['name'], '1.49'])
            total += 1.49
        elif item['type'] == 'meal':
            if item['size'] == 'Small':
                price = 5.99
            elif item['size'] == 'Medium':
                price = 6.99
            else:
                price = 7.99
            rows.append([f'{item["sandwich"]} {item["size"]} meal with {item["drink"]}', f'{price:.2f}'])
            total += price
    rows.append(['Total', f'{total:.2f}'])
    invoice = '\n'.join([','.join(row) for row in rows])
    return invoice