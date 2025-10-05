print("===== Bagel's Place Menu =====")
print("1. Pizza  -  $15.99")
print("2. Burger -  $12.50")
print("3. Salad  -  $9.99")
print("4. Pasta  -  $13.75")
print("5. Bagel  -  $11.11")

num = int(input("Choose a menu item # (1-5)"))

if num == 1:
    food = "Pizza - $15.99"
    price = 15.99
elif num == 2:
    food = "Burger - $12.50"
    price = 12.50
elif num == 3:
    food = "Salad - $9.99"
    price = 9.99
elif num == 4:
    food = "Pasta - $13.75"
    price = 13.75
elif num == 5:
    food = "Bagel - $11.11"
    price = 11.11
else:
    print("Please enter a number 1-5")

drink = input("Would you like a drink? (+2.50) (yes/no) :").strip().lower()

if drink == "yes":
    drink_price = 2.50
else:
    drink_price = 0

subtotal = price + drink_price
tax = round(subtotal * 0.08, 2)
total = round(subtotal + tax, 2)

print("=== Your Order ===")
print(f"Food:       {food}")
print(f"Drink:      {'Yes' if drink_price > 0 else 'No'} - ${drink_price}")
print(f"Subtotal:   ${subtotal}")
print(f"Tax (8%):   ${tax}")
print(f"Total:      ${total}")

    
    
    
    


