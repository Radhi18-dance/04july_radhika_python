def palindrome(str):
    str=input('Enter A String: ')
    if str == str[::-1]:
        print(f'The String "{str}" is a palindrome.')
    else:
        print(f'The String "{str}" is Not palindrome.')


palindrome(str)