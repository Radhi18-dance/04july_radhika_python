mydict={}
n = int(input("Enter the size of the dictionary: "))

for i in range(n):
    key = input(f"Enter {i+1} key: ")
    val = input(f"Enter {i+1} value: ")
    mydict[key] = val

print("Dictionary is:", mydict)
search_key=input("enter key to search :")
if search_key in mydict:
    print(f"The key '{search_key}' exists in the dictionary.")
else:
    print(f"The key '{search_key}' does not exist in the dictionary.")