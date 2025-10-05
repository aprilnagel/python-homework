print("Welcome to Bagel Theatre! To purchase a ticket, please enter your info below:")


    
name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
 
try: 
    if age <= 13:
        price_per_ticket = 8 
    elif age >= 13 and age < 64:
        price_per_ticket = 12
    elif age >= 65:
         price_per_ticket = 9
except ValueError:
    print("Please enter valid age")

quantity = int(input("How many tickets do you want? "))
    
total = (age * quantity)

print("🎟️ Movie Ticket Receipt 🎟️")
print(f"Customer name:  {name}")
print(f"Ticket type:    {"Child ($8.00)" if age <= 13 else "Adult ($12.00)" if age >= 13 and age < 64 else "Senior ($9.00)"}")
print(f"Quantity:       {quantity} ")    
print(f"Total:          ${total}")
print("Thank you for your purchase! Enjoy your movie!")
