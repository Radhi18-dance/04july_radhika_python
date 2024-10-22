try:
    num=int(input("enter number:"))
    if num%2!=0:
        print("Number is odd:")
    else:
        raise ValueError("not odd number")
except Exception as e:
    print(e)