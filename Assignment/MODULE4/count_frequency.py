file = open('stdata.txt', 'r')
d = {}
for i in file:
    words = i.strip().split()
    for j in words:
        j = j.lower()# Convert to lowercase to ensure case insensitivity
        if j in d: # Count the frequency of each word
            d[j] += 1
        else:
            d[j] = 1

# Close the file after reading
file.close()

# Print the word frequencies
for r in d.keys():
    print(r, ":", d[r])
