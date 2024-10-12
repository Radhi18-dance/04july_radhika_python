def check_range():
    num = int(input("Enter a number: "))
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
#if check_range in range(start,end)
    if start <= num <= end:
        print(f"{num} is in the range {start}to {end}")
    else:
        print(f"{num} is not in the range {start}to {end}")

check_range()