# 1. *Create a function* that takes an array, an index, and a value as parameters.
#    Inside the function, use the insert method to insert the value at the specified index in the array. 
#    Return the modified array.
# 2. *Implement a simple shopping cart program* using an array.
#     Create functions to add items, remove items, and update quantities using array methods. 
#     Print the cart's contents after each operation.
# 3. *Write a program* that uses a while loop to print the first 25 integers.
# 4. *Write a program* that uses a while loop to print the first 10 even numbers.
# 5. *Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.
# 6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
# 7. *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.
# 8. *Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
# 9. *Write a program* to remove all the odd numbers from an array.

# =====================================================================================================
print(""" 1. *Create a function* that takes an array, an index, and a value as parameters.
    Inside the function, use the insert method to insert the value at the specified index in the array. 
    Return the modified array.""")

def insert_at_index(arr, value, index):
    arr.insert(index, value)
    return arr

numbers = [10,1,2,5,10, 12, 8, 6]
modified_array = insert_at_index(numbers, 786, 3)

print("Modified array:", modified_array)

# =====================================================================================================
print(""" 2. *Implement a simple shopping cart program* using an array.
    Create functions to add items, remove items, and update quantities using array methods. 
    Print the cart's contents after each operation.""")

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


# =====================================================================================================
print(""" 3. *Write a program* that uses a while loop to print the first 25 integers.""")
i = 1
while i <=25:
  print(i)
  i += 1

# =====================================================================================================
print(""" 4. *Write a program* that uses a while loop to print the first 10 even numbers.""")

num1 = 0
while num1 <= 20:
  num1 += 1
  if (num1%2 == 0):
    print(num1)
  


# =====================================================================================================
print(""" 5. Create a function* that takes a positive integer as a parameter and uses a while loop 
    to calculate and return the factorial of that number.""")

def factorial(n):
    if n < 0:
        return "Please Enter positive Intiger Value."
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    
    return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")

# =====================================================================================================
print(""" 6. *Write a program* that has an array of numbers; if the number is negative, 
    it should remove the negative number from the array.""")
def remove_negatives(arr):
      for num in arr[:]:
        if num < 0:
            arr.remove(num)

numbers = [10,-1,100,111,-77, -5, 12, -3, 8, -7, 6]

remove_negatives(numbers)

print("Array without negatives:", numbers)
# =====================================================================================================
print(""" 7. *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate 
       and return the sum of all the numbers in the array.""")
def sum_of_array(arr):
    total_sum = 0
    i = 0
    while i < len(arr):
        total_sum += arr[i]
        i += 1
    return total_sum

numbers = [10, 5, 7, 3, 8]
result = sum_of_array(numbers)
print("Sum of the array:", result)
# =====================================================================================================
print(""" 8. Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array.
     Use a while loop to perform the conversion for each temperature..""")
# Function to convert a list of temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    i = 0
    while i < len(celsius_list):
        fahrenheit = (celsius_list[i] * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
        i += 1
    return fahrenheit_list


celsius_list = list(map(float, input("Enter temperatures in Celsius (separated by spaces): ").split()))
converted_temperatures = celsius_to_fahrenheit(celsius_list)
print("Temperatures in Fahrenheit:", converted_temperatures)


# =====================================================================================================
print(""" 9. *Write a program* to remove all the odd numbers from an array.""")

def remove_odd(arr):
      for num in arr[:]:
        if num%2 != 0:
            arr.remove(num)

numbers = [10,1,100,111,77,5,12,23,18,27,16]
remove_odd(numbers)
print("Array without Odd Numbers:", numbers)