# Using for loop to check even odd number

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Get input from the user
count = int(input("How many numbers do you want to check? "))

# Iterate for each number
for i in range(count):
    num = int(input("Enter number {}: ".format(i+1)))
    result = check_even_odd(num)
    print("Number {} is {}".format(num, result))