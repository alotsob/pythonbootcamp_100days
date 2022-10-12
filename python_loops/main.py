
# fruits = ["apple", "pawpaw", "orange", "pear", "mango"]
# for fruit in fruits:
#     print(fruit)

fruits = ["apple", "peach", "pear"]
for fruit in fruit:
    print(fruit)
    print(fruit + "pie")
print(fruits)    

#for loop with range

for number in range( 1, 11):
    print(number)
# skips by 3
for number in range( 1, 11, 3):
    print(number)    

# adding total in range
total = 0
for number in range(1, 101):
    total  += number
print(total)    