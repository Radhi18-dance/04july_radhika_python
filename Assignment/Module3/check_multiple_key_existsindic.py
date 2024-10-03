my_dict = {}
key_search=[]

n = int(input("Enter the size of the dictionary: "))

for i in range(n):
    key = input(f"Enter {i+1} key: ")
    val = input(f"Enter {i+1} value: ")
    my_dict[key] = val

print("Dictionary is:", my_dict)

m = int(input("Enter the number of keys to search for: "))

for i in range(m):
    k = input(f"Enter {i+1} key to search for: ")
    key_search.append(key)
for k in key_search:
    if k in key_search:
        print("key exist in the dictionary.")
    else:
        print("key not  exist in the dictionary.")