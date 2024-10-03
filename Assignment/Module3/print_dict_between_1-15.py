mydict={}
n = int(input("Enter the size of the dictionary: "))
'''if n<=15:
    for i in range(n):
        key = input(f"Enter {i+1} key: ")
        val = input(f"Enter {i+1} value: ")
        mydict[key] = val
    print(mydict)'''
'''else:
    print("enter valid size")'''
# Create an empty dictionary

for i in range(1, 16):
    val = input(f"Enter value for key {i}: ")
    mydict[i] = val


print("Dictionary is:", mydict)