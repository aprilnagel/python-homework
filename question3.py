
print("1. Dog")
print("2. Cat")
print("3. Bird")
print("4. Hamster")

pet_num = int(input("What kind of pet do you have? (1-4) "))

if pet_num == 1:
    pet_type = "dog"
elif pet_num == 2:
    pet_type = "cat"
elif pet_num == 3:
    pet_type = "bird"
elif pet_num == 4:
    pet_type = "hamster"
else:
    print("Please choose a number between 1-4")

human_age = int(input("How old is your pet in human years? "))
 
if pet_type == "dog":
    if human_age <= 2:
        pet_age = 12 * human_age
    else:
        pet_age = 24 + (human_age - 2) * 4
if pet_type == "cat": 
    if human_age <= 2:
        pet_age = 12 * human_age
    else:
        pet_age = 24 + (human_age - 2) * 4
if pet_type == "bird":
    pet_age = human_age * 9
elif pet_type == "hamster":
    pet_age = human_age * 25
    

print("==== Pet age conversion ====")
print(f"Pet Type:       {pet_type}")
print(f"Human Age:      {human_age} year(s)")
print(f"Pet Age:        {pet_age} pet years!")
print(f"Fun Fact:       Your {pet_type} is like a {pet_age} year old human!")





    




