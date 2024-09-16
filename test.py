shopping_cart = []

def add_item(cart, item, quantity):
    for i in range(len(cart)):
        if cart[i]['item'] == item:
            cart[i]['quantity'] += quantity
            print(f'Updated {item} quantity to {cart[i]["quantity"]}.')
            print_cart(cart)
            return
    cart.append({'item': item, 'quantity': quantity})
    print(f'Added {quantity} of {item} to the cart.')
    print_cart(cart)

def remove_item(cart, item):
    for i in range(len(cart)):
        if cart[i]['item'] == item:
            cart.pop(i)
            print(f'Removed {item} from the cart.')
            print_cart(cart)
            return
    print(f'{item} not found in the cart.')
    print_cart(cart)

def update_quantity(cart, item, quantity):
    for i in range(len(cart)):
        if cart[i]['item'] == item:
            cart[i]['quantity'] = quantity
            print(f'Updated {item} quantity to {quantity}.')
            print_cart(cart)
            return
    print(f'{item} not found in the cart.')
    print_cart(cart)

def print_cart(cart):
    if not cart:
        print("The cart is empty.")
    else:
        print("Shopping Cart Contents:")
        for entry in cart:
            print(f"{entry['item']}: {entry['quantity']}")
    print("-" * 30)

add_item(shopping_cart, 'Apple', 3)
add_item(shopping_cart, 'Banana', 2)
add_item(shopping_cart, 'Mango', 2)
add_item(shopping_cart, 'pinapple', 2)
update_quantity(shopping_cart, 'Apple', 9)
remove_item(shopping_cart, 'Banana')
add_item(shopping_cart, 'Orange', 4)
