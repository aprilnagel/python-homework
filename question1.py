print("Welcome to Bagel Theatre! To purchase a ticket, please enter your age below")

age = int(input("Enter your age: "))

if age <= 13:
    print("Child ticket (under 13): $8")
elif age >= 13 and age < 64:
    print("Adult ticket (13-64): $12 ")
elif age >= 65:
    print("Senior ticket (+65): $9")
else:
    print("Please enter a valid age")