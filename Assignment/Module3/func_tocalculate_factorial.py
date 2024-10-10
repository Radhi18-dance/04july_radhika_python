def factorial():
    no=int(input("enter number to find factorial:"))
    factorial=1
    for i in range(1,no+1):
        factorial=factorial*i
    print(f'factorial of{no} is{factorial}')
factorial()