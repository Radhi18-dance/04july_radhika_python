my_dict = {}

n = int(input("Enter the size of the dictionary: "))

for i in range(n):
    key = input(f"Enter {i+1} key: ")
    val = input(f"Enter {i+1} value: ")
    my_dict[key] = val

print("Dictionary is:", my_dict)

m = int(input("Enter the number of keys to search for: "))

keys_to_search = []
for i in range(m):
    key = input(f"Enter key {i+1} to search for: ")
    keys_to_search.append(key)

all_keys_exist = all(key in my_dict for key in keys_to_search)

if all_keys_exist:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")