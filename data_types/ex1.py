
two_digit_number = input("Type a two digit number: ")

#check data type of tw digits
print(type(two_digit_number))

#Get first and second digits using subscripting, then cnvert using int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits together
two_digit_number = second_digit + first_digit
print(two_digit_number)
