

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

number_items = len(names)
random_choice(0, number_items -1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + "is going to buy the meal today")