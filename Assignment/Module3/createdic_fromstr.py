str=input("enter string:")
letter_count={}
for i in str:
    if i in letter_count:
        letter_count[i] += 1
    else:
        letter_count[i] = 1

print(f'String: {str}')

print(letter_count)