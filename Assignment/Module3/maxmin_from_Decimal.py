num_count = int(input("Enter the number of decimal numbers: "))
decimal_numbers = []

for i in range(num_count):
    num = float(input(f"Enter decimal number {i+1}: "))
    decimal_numbers.append(num)

max_num = max(decimal_numbers)
min_num = min(decimal_numbers)

print(f"The decimal numbers are: {decimal_numbers}")
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")